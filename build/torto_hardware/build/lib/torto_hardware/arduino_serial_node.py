#!/usr/bin/env python3

import numpy as np
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Quaternion
from torto_interfaces.msg import TortoJointAngles
import serial
import time
import math
from torto_hardware.servo_driver.servo_calibration import anglesConfig
from torto_hardware.imu_driver.mpu6050_calibration import SensorCalibration


class SerialNode(Node):
    
    def __init__(self):
        super().__init__('arduino_serial')
    
        self.angle_config = anglesConfig()
        self.calibration = SensorCalibration()

        self.calibrated = False
        self.waiting_to_start_calibrate = True
        self.calibration_samples = 2000  # Number of samples to take for calibration
        self.roll_sum, self.pitch_sum, self.yaw_sum = 0, 0, 0
        self.sample_count = 0

        # Initialize the serial port
        try:
            self.serial_port = serial.Serial('/dev/serial/by-id/usb-1a86_USB_Serial-if00-port0', baudrate=115200, timeout=0.1)
            time.sleep(2) 
            self.get_logger().info('Serial port connected!')
        except serial.SerialException as e:
            self.get_logger().error(f"Error connecting to serial port: {e}")
            self.serial_port = None  # Ensure self.serial_port does not remain undefined
            return  # Stop execution if serial connection fails

        self.publisher_ = self.create_publisher(Imu, '/imu/data', 10)
        self.torto_motor_angles_publisher = self.create_publisher(TortoJointAngles, "torto_motor_angles", 10)

        # Timer
        self.timer = self.create_timer(0.02, self.arduino_sensors_callback)
        self.send_timer = self.create_timer(0.02, self.send_angles_to_arduino)
        self.sendMotor_timer = self.create_timer(0.02, self.publish_torto_motorAngles)

        self.roll = 0
        self.pitch = 0
        self.yaw = 0
        self.trueRoll = 0
        self.truePitch = 0
        self.trueYaw = 0
        self.accelx = 0
        self.accely = 0
        self.accelz = 0
        self.gyrox = 0
        self.gyroy = 0
        self.gyroz = 0
        self.pm1 = 0
        self. pm2_5 = 0
        self. pm10 = 0
        self.angles = np.asarray([[90.,  90., 0.], 
                                    [90.,  90., 0.], 
                                    [90.,  90., 0.], 
                                    [90.,  90., 0.]])
        self.adjusted_angles = self.angle_config.calibrate_angles(self.angles) 
                                            
        self.subscriber_ = self.create_subscription(TortoJointAngles, "torto_joint_angles", self.callback_TORTO_Joint_Angles, 10)
        self.send_command('relay', 'ON')  # Assuming 'relay' state is 'ON'


    def arduino_sensors_callback(self):
        """Read data from Arduino and publish to ROS 2 topic."""
        if self.serial_port is None or not self.serial_port.is_open:
            self.get_logger().error("Serial port not open. Cannot read data.")
            return

        try:
            while self.serial_port.in_waiting:
                data = self.serial_port.readline().decode('utf-8', errors='ignore').strip()

                if "ANGLES:" in data:
                    return  
                
                if "MPU:" in data:
                    mpu_data = str(data.split("PMS:")[0].replace("MPU:", "").strip())
                    mpu_data_dict = {item.split(":")[0]: int(item.split(":")[1]) for item in mpu_data.strip(',').split(",")}
                    
                    self.roll = int(mpu_data_dict['Roll'])/100
                    self.pitch = int(mpu_data_dict['Pitch'])/100
                    self.yaw = int(mpu_data_dict['Yaw'])/100
                    self.accelx = int(mpu_data_dict['AX'])
                    self.accely = int(mpu_data_dict['AY'])
                    self.accelz = int(mpu_data_dict['AZ'])
                    self.gyrox = int(mpu_data_dict['GX'])
                    self.gyroy = int(mpu_data_dict['GY'])
                    self.gyroz = int(mpu_data_dict['GZ'])
                
                if  self.waiting_to_start_calibrate:
                    print("setting MPU6050 for 4 seconds")
                    time.sleep(4)
                    self.waiting_to_start_calibrate = False
                    print("MPU6050 is Done Setting")
                    
                elif not self.calibrated and not self.waiting_to_start_calibrate:
                    self.roll_sum += self.roll
                    self.pitch_sum += self.pitch
                    self.yaw_sum += self.yaw
                    self.sample_count += 1
                    if self.sample_count % 100 == 0:
                        self.get_logger().info(f"Calibration not complete. Skipping sensor data processing, {self.sample_count:.2f} points so far")

                    # If we have enough samples, calculate offsets
                    if self.sample_count >= self.calibration_samples:
                        self.calibration.calibrate(self.roll_sum, self.pitch_sum, self.yaw_sum, self.sample_count)
                        self.calibrated = True
                else:
                    self.trueRoll, self.truePitch, self.trueYaw = self.calibration.apply_calibration(self.roll, self.pitch, self.yaw)
                self.publish_torto_imu()
        except Exception as e:
            self.get_logger().error(f"Error reading from Arduino: {e}")

    def send_command(self, command_type, data):
        """Send the specified command (angles or relay) to Arduino."""
        if self.serial_port is None or not self.serial_port.is_open:
            self.get_logger().error("Serial port not open. Cannot send command.")
            return

        try:
            if command_type == "angles":
                # Apply the angle offset using angle_config
                self.adjusted_angles = self.angle_config.calibrate_angles(data) 
                
                # Format the adjusted angles as required by the Arduino
                angle_str = ' '.join([','.join(map(str, angles)) for angles in self.adjusted_angles])
                command = f"ANGLES:{angle_str}\n"
                self.serial_port.write(command.encode('utf-8'))
                
            elif command_type == "relay":
                if data not in ['ON', 'OFF']:
                    self.get_logger().error(f"Invalid relay state: {data}")
                    return
                command = f"RELAY:{data}\n"
                self.serial_port.write(command.encode('utf-8'))

            else:
                self.get_logger().error(f"Invalid command type: {command_type}")

        except Exception as e:
            self.get_logger().error(f"Error sending command to Arduino: {e}")

    def callback_TORTO_Joint_Angles(self, msg):
        self.angles = np.asarray([[msg.theta_deg_fr_detoid,  msg.theta_deg_fr_femur, msg.theta_deg_fr_tibia], 
                                  [msg.theta_deg_fl_detoid,  msg.theta_deg_fl_femur, msg.theta_deg_fl_tibia], 
                                  [msg.theta_deg_br_detoid,  msg.theta_deg_br_femur, msg.theta_deg_br_tibia], 
                                  [msg.theta_deg_bl_detoid,  msg.theta_deg_bl_femur, msg.theta_deg_bl_tibia]])

    def send_angles_to_arduino(self):
        """Periodically send the latest joint angles to the Arduino."""
        if hasattr(self, 'angles'):
            self.send_command('angles', self.angles)

    def publish_torto_imu(self):
        roll = math.radians(self.trueRoll)
        pitch = math.radians(self.truePitch)
        yaw = math.radians(self.trueYaw)
        qx, qy, qz, qw = self.euler_to_quaternion(roll, pitch, yaw)
        imu_msg = Imu()
        imu_msg.header.stamp = self.get_clock().now().to_msg()
        imu_msg.header.frame_id = 'tortoIMU_link'
        imu_msg.orientation = Quaternion(x=qx, y=qy, z=qz, w=qw)
        imu_msg.angular_velocity.x = float(math.radians(self.gyrox / 131.0))
        imu_msg.angular_velocity.y = float(math.radians(self.gyroy / 131.0))
        imu_msg.angular_velocity.z = float(math.radians(self.gyroz / 131.0))
        imu_msg.linear_acceleration.x = float(self.accelx * 9.80665 / 16384.0)
        imu_msg.linear_acceleration.y = float(self.accely * 9.80665 / 16384.0)
        imu_msg.linear_acceleration.z = float(self.accelz * 9.80665 / 16384.0)
        imu_msg.orientation_covariance[0] = 0.01
        imu_msg.angular_velocity_covariance[0] = 0.01
        imu_msg.linear_acceleration_covariance[0] = 0.1
        self.publisher_.publish(imu_msg)

    def publish_torto_motorAngles(self):
        msg = TortoJointAngles()
        msg.theta_deg_fr_detoid = float(self.adjusted_angles[0][0])
        msg.theta_deg_fr_femur = float(self.adjusted_angles[0][1])
        msg.theta_deg_fr_tibia = float(self.adjusted_angles[0][2])
        msg.theta_deg_fl_detoid = float(self.adjusted_angles[1][0])
        msg.theta_deg_fl_femur = float(self.adjusted_angles[1][1])
        msg.theta_deg_fl_tibia = float(self.adjusted_angles[1][2])
        msg.theta_deg_br_detoid = float(self.adjusted_angles[2][0])
        msg.theta_deg_br_femur = float(self.adjusted_angles[2][1])
        msg.theta_deg_br_tibia = float(self.adjusted_angles[2][2])
        msg.theta_deg_bl_detoid = float(self.adjusted_angles[3][0])
        msg.theta_deg_bl_femur = float(self.adjusted_angles[3][1])
        msg.theta_deg_bl_tibia = float(self.adjusted_angles[3][2])
        self.torto_motor_angles_publisher.publish(msg)

    def euler_to_quaternion(self, roll, pitch, yaw):
        # Inputs must be in radians
        qx = math.sin(roll/2) * math.cos(pitch/2) * math.cos(yaw/2) - math.cos(roll/2) * math.sin(pitch/2) * math.sin(yaw/2)
        qy = math.cos(roll/2) * math.sin(pitch/2) * math.cos(yaw/2) + math.sin(roll/2) * math.cos(pitch/2) * math.sin(yaw/2)
        qz = math.cos(roll/2) * math.cos(pitch/2) * math.sin(yaw/2) - math.sin(roll/2) * math.sin(pitch/2) * math.cos(yaw/2)
        qw = math.cos(roll/2) * math.cos(pitch/2) * math.cos(yaw/2) + math.sin(roll/2) * math.sin(pitch/2) * math.sin(yaw/2)
        return [qx, qy, qz, qw]

    def destroy_node(self):
        """Ensure serial port is closed on shutdown."""
        if self.serial_port is not None and self.serial_port.is_open:
            self.serial_port.close()
            self.get_logger().info("Serial port closed.")
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = SerialNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Node terminated.')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
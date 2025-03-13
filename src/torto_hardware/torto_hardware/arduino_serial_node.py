#!/usr/bin/env python3

import numpy as np
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from torto_interfaces.msg import TortoJointAngles
import serial
import time
from torto_hardware.servo_calibration import anglesConfig


class SerialNode(Node):
    
    def __init__(self):
        super().__init__('arduino_serial')

        # Initialize angles_config for angle adjustment
        self.angle_config = anglesConfig()

        # Initialize the serial port
        try:
            self.serial_port = serial.Serial('/dev/serial/by-id/usb-1a86_USB_Serial-if00-port0', baudrate=115200, timeout=1)
            self.get_logger().info('Serial port connected!')
        except serial.SerialException as e:
            self.get_logger().error(f"Error connecting to serial port: {e}")
            self.serial_port = None  # Ensure self.serial_port does not remain undefined
            return  # Stop execution if serial connection fails

        self.publisher_ = self.create_publisher(String, 'sensor_data', 10)
        self.torto_motor_angles_publisher = self.create_publisher(TortoJointAngles, "torto_motor_angles", 10)

        # Timer
        self.timer = self.create_timer(0.02, self.arduino_sensors_callback)
        self.send_timer = self.create_timer(0.02, self.send_angles_to_arduino)
        self.sendMotor_timer = self.create_timer(0.02, self.publish_torto_motorAngles)

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
            if self.serial_port.in_waiting > 0:
                data = self.serial_port.readline().decode('utf-8').strip()
                self.get_logger().info(f"Received from Arduino: {data}")

                # Create and publish ROS 2 String message
                sensorsMsg = String()
                sensorsMsg.data = data
                self.publisher_.publish(sensorsMsg)
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
                self.get_logger().info(f"Sent adjusted angles command to Arduino: {command.strip()}")
                
            elif command_type == "relay":
                if data not in ['ON', 'OFF']:
                    self.get_logger().error(f"Invalid relay state: {data}")
                    return
                command = f"RELAY:{data}\n"
                self.serial_port.write(command.encode('utf-8'))
                self.get_logger().info(f"Sent relay command to Arduino: {command.strip()}")

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
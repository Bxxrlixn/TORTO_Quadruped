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

        # Initialize angle calibration
        self.angle_config = anglesConfig()

        # Initialize serial connection
        self.serial_port = self.init_serial('/dev/serial/by-id/usb-1a86_USB_Serial-if00-port0', 115200)

        # ROS 2 Publisher & Subscribers
        self.publisher_ = self.create_publisher(String, 'sensor_data', 10)
        self.subscriber_ = self.create_subscription(TortoJointAngles, "torto_joint_angles", self.callback_TORTO_Joint_Angles, 10)

        # Timers
        self.create_timer(0.01, self.arduino_sensors_callback)
        self.create_timer(0.01, self.send_angles_to_arduino)

        # Default angles (90° neutral position)
        self.angles = np.asarray([[90. , 90. , 0.],
                                  [90. , 90. , 0.],
                                  [90. , 90. , 0.],
                                  [90. , 90. , 0.]])

        # Send initial relay command
        self.send_command('relay', 'ON')

    def init_serial(self, port, baudrate):
        """Initialize serial connection."""
        try:
            serial_port = serial.Serial(port, baudrate=baudrate, timeout=1)
            self.get_logger().info('Serial port connected!')
            return serial_port
        except serial.SerialException as e:
            self.get_logger().error(f"Error connecting to serial port: {e}")
            return None  # Serial connection failed

    def arduino_sensors_callback(self):
        """Read and publish sensor data from Arduino."""
        if not self.serial_port or not self.serial_port.is_open:
            self.get_logger().error("Serial port not open. Cannot read data.")
            return

        try:
            if self.serial_port.in_waiting > 0:
                data = self.serial_port.readline().decode('utf-8').strip()
                self.publisher_.publish(String(data=data))
        except Exception as e:
            self.get_logger().error(f"Error reading from Arduino: {e}")

    def send_command(self, command_type, data):
        """Send command (angles or relay) to Arduino."""
        if not self.serial_port or not self.serial_port.is_open:
            self.get_logger().error("Serial port not open. Cannot send command.")
            return

        try:
            if command_type == "angles":
                adjusted_angles = self.angle_config.calibrate_angles(data) 
                angle_str = ' '.join([','.join(map(str, angles)) for angles in adjusted_angles])
                command = f"ANGLES:{angle_str}\n"
            elif command_type == "relay" and data in ['ON', 'OFF']:
                command = f"RELAY:{data}\n"
            else:
                self.get_logger().error(f"Invalid command: {command_type} - {data}")
                return

            self.serial_port.write(command.encode('utf-8'))
        except Exception as e:
            self.get_logger().error(f"Error sending command: {e}")

    def callback_TORTO_Joint_Angles(self, msg):
        """Update joint angles from ROS 2 topic message."""
        self.angles = np.array([
            [msg.theta_deg_fr_detoid, msg.theta_deg_fr_femur, msg.theta_deg_fr_tibia],
            [msg.theta_deg_fl_detoid, msg.theta_deg_fl_femur, msg.theta_deg_fl_tibia],
            [msg.theta_deg_br_detoid, msg.theta_deg_br_femur, msg.theta_deg_br_tibia],
            [msg.theta_deg_bl_detoid, msg.theta_deg_bl_femur, msg.theta_deg_bl_tibia]
        ])


    def send_angles_to_arduino(self):
        """Send joint angles to Arduino periodically."""
        if hasattr(self, 'angles'):
            self.send_command('angles', self.angles)

    def destroy_node(self):
        """Close serial port on shutdown."""
        if self.serial_port and self.serial_port.is_open:
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

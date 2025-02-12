#!/usr/bin/env python3

import numpy as np
import rclpy
from rclpy.node import Node
from torto_ctrl.adaptive_gait.dynamic_gait import dynamicGait
from torto_ctrl.kinematic_model.transformation_model import tortoTransformationModel
from torto_ctrl.kinematic_model.adaptive_limb import tortoAdaptiveLimb
from torto_interfaces.msg import TortoJointAngles

class TortoControllerNode(Node):
    def __init__(self):
        super().__init__("torto_Controller")
        self.adpt_gait = dynamicGait()
        self.tf_Model = tortoTransformationModel() 
        self.adpt_Limb = tortoAdaptiveLimb()
        self.torto_joint_angles_publisher = self.create_publisher(TortoJointAngles, "torto_joint_angles", 10)
        self.get_logger().info('TORTO Joint Angles Activated')

        self.angles_FR = np.array([90. , 90. , 0.])
        self.angles_FL = np.array([90. , 90. , 0.])
        self.angles_BR = np.array([90. , 90. , 0.])
        self.angles_BL = np.array([90. , 90. , 0.])
        # Gait params
        self.Vx = 0
        self.Vy = 0
        self.Vz = 0
        self.Wrot = -0.4
        self.angle_FR = 0
        self.angle_FL = 0
        self.angle_BR = 0
        self.angle_BL = 0
        self.step_offset = 0.75
        self.T = 1.6 #period of time (in seconds) of every step
        self.offset = np.array([0. , 0.5 , 0.5 , 0.]) 
        self.body_Foot_Initial = np.asarray([[0.136635,  -0.1121875, -0.14], 
                                             [0.136635,  0.1121875, -0.14], 
                                             [-0.136635,  -0.1121875, -0.14], 
                                             [-0.136635,  0.1121875, -0.14]])
        # Limb transformation params
        self.Foot_Position = np.asarray([[0, 0, 0], 
                                         [0, 0, 0], 
                                         [0, 0, 0], 
                                         [0, 0, 0]])
        # Body transformation params
        self.body_orientation = np.asarray([0, 0, 0])
        self.body_position = np.asarray([0, 0, 0])


        self.create_timer(0.02, self.control_loop)



    def publish_torto_jointAngles(self):
        msg = TortoJointAngles()
        msg.theta_deg_fr_detoid = self.angles_FR[0]
        msg.theta_deg_fr_femur = self.angles_FR[1]
        msg.theta_deg_fr_tibia = self.angles_FR[2]
        msg.theta_deg_fl_detoid = self.angles_FL[0]
        msg.theta_deg_fl_femur = self.angles_FL[1]
        msg.theta_deg_fl_tibia = self.angles_FL[2]
        msg.theta_deg_br_detoid = self.angles_BR[0]
        msg.theta_deg_br_femur = self.angles_BR[1]
        msg.theta_deg_br_tibia = self.angles_BR[2]
        msg.theta_deg_bl_detoid = self.angles_BL[0]
        msg.theta_deg_bl_femur = self.angles_BL[1]
        msg.theta_deg_bl_tibia = self.angles_BL[2]
        self.torto_joint_angles_publisher.publish(msg)


    def control_loop(self):
        body_Foot  = self.adpt_gait.step_Loop(self.Vx, self.Vy, self.Vz, self.angle_FR, self.angle_FL, self.angle_BR, self.angle_BL, self.Wrot, self.T, self.step_offset, self.offset, self.body_Foot_Initial)
        body_Foot = self.adpt_Limb.foot_tranformed_pose(self.Foot_Position, body_Foot)
        tf_Model_angles = self.tf_Model.angles_from_pose(self.body_orientation, self.body_position, body_Foot)
        self.angles_FR = tf_Model_angles[0]
        self.angles_FL = tf_Model_angles[1]
        self.angles_BR = tf_Model_angles[2]
        self.angles_BL = tf_Model_angles[3]
        self.body_Foot = tf_Model_angles[4]
        self.publish_torto_jointAngles()
        self.get_logger().info(f"{tf_Model_angles}")

def main(args=None):
    rclpy.init(args=args)
    node = TortoControllerNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Node terminated.')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

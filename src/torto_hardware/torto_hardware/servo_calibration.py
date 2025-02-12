#!/usr/bin/env python3

import numpy as np
import math as m

class anglesConfig:
    def __init__(self):
        # Assuming there are 12 values for 4 legs (3 servos per leg)
        self.offset = [-182.5, 5, -185, 2, -190, -5, -3, -175, -10, -175, 0, -180]

    def set_offset(self, offset):
        self.offset = offset

    def map_angles(self, x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


    def calibrate_angles(self, angles):
        # angles should be a list of lists: [ [angle1, angle2, angle3], [angle1, angle2, angle3], ... ]
        adjusted_angles = []
        for leg in range(4):
            leg_angles = angles[leg]
            # Apply offset for each joint in the leg
            adjusted_leg_angles = [abs(leg_angles[i] + self.offset[leg * 3 + i]) for i in range(3)]
            #Maximum servo angle:0, Minimum servo angle: 180, 3205 corresponds to pulse step at 2.5ms(100% duty cycle), 641 corresponds to pulse step at 0.5ms(0% duty cycle)
            mapped_leg_angles = [self.map_angles(adjusted_leg_angles[i], 0, 180, 641, 3205) for i in range(3)] 
            rounded_leg_angles = [int(round(mapped_leg_angles[i])) for i in range(3)]
            adjusted_angles.append(rounded_leg_angles)
        return adjusted_angles

#!/usr/bin/env python3

import numpy as np
import math as m

class anglesConfig:
    def __init__(self):
        # Assuming there are 12 values for 4 legs (3 servos per leg)
        self.offset = [-182.5, 5, -185, 2, -190, -5, -3, -175, -10, -175, 0, -180]

    def set_offset(self, offset):
        self.offset = offset

    def calibrate_angles(self, angles):
        # angles should be a list of lists: [ [angle1, angle2, angle3], [angle1, angle2, angle3], ... ]
        adjusted_angles = []
        for leg in range(4):
            leg_angles = angles[leg]
            # Apply offset for each joint in the leg
            adjusted_leg_angles = [abs(leg_angles[i] + self.offset[leg * 3 + i]) for i in range(3)]
            rounded_leg_angles = [int(round(adjusted_leg_angles[i])) for i in range(3)]
            adjusted_angles.append(rounded_leg_angles)
        return adjusted_angles

#!/usr/bin/env python3

import sys
import numpy as np
from torto_ctrl.transformation_kinematic import tortoTransformation_kinematic


y = tortoTransformation_kinematic() 

def main():
        x = y.angles_from_pose([0, 0, 0], [0, 0, 0], [[0.136635,  -0.1121875, -0.14], [0.136635,  0.1121875, -0.14], [-0.136635,  -0.1121875, -0.14], [-0.136635,  0.1121875, -0.14]])
        sys.stdout.write(str(x))  # Convert output to string before writing
    
if __name__ == '__main__': 
    main() 

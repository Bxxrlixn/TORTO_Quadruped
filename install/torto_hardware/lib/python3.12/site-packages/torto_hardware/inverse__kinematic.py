#!/usr/bin/env python3

import numpy as np

class InverseKinematic:
    def __init__(self):
        pass  # No instance variables needed, but you can initialize some if required.

    def check_domain(self, D, limit=0.999):
        """Clamp D between -1 and 1 to prevent domain errors."""
        return max(min(D, limit), -limit)

    def calculate_angles(self, x, y, z):
        """Calculate inverse kinematics angles for a leg given (x, y, z) position."""
        D = np.sqrt((z ** 2) + (y ** 2) - 1788.021)
        DetoidAngle = np.arctan2(z, y) + np.arctan2(D, 42.285)
        
        H = np.sqrt((x ** 2) + (D ** 2))
        phi = np.arccos(self.check_domain(((H ** 2) - 16200) / -16200))

        zeta = np.arctan2(x, D) + np.arcsin(self.check_domain((90 * np.sin(phi)) / H))
        
        I = np.sqrt((9700) - (7200 * np.cos(phi)))
        K = np.arccos(self.check_domain(((I ** 2) - 8676) / (-4320)))

        C = np.arcsin(self.check_domain((40 * np.sin(phi)) / I)) + np.arcsin(self.check_domain((90 * np.sin(K)) / I))

        TibiaAngle = np.pi / 2 - (C - zeta)

        L = 4.0037853041 - C - TibiaAngle

        J = np.sqrt((3127.24) - (2988 * np.cos(L)))
        M = np.arccos(self.check_domain(((J ** 2) - 2601) / (-2160)))

        N = np.arcsin(self.check_domain((45 * np.sin(L)) / J)) + np.arcsin(self.check_domain((45 * np.sin(M)) / J))

        FemurAngle = 3.8519416592 - N

        return {
            "DetoidAngle": np.degrees(DetoidAngle),
            "FemurAngle": np.degrees(FemurAngle),
            "TibiaAngle": np.degrees(TibiaAngle)
        }

# Example usage
# ik = InverseKinematic()
# angles = ik.calculate_angles(50, 100, 150)
# print(angles)
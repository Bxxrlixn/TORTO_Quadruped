
import time
import numpy as np
from evdev import InputDevice, categorize, ecodes  # pip install evdev
from ps5_Button import ButtonStatus

class QuadrupedController:
    def __init__(self, device_path):
        self.buttons_state = ButtonStatus()
        self.gamepad = InputDevice(device_path)
    
        # Mode_status
        self.mode = {"X": True, "square": False, "triangle": False, "circle": False }
        self.submode = {"l1": False, "l2": False, "r1": False, "r2": False, "pause": False, "share": False}
        self.subsubmode = {'up': False, 'down': False, 'left': False, 'right': False}
        self.idcrease = {'increase': False, 'decrease': False}
        self.wrot_status = {"left": False, "right": False}
        
        # TORTO parameters
        # Mode square
        self.Vx = 0 #out put velocity
        self.Vy = 0
        self.Vz = 0
        self.Ux = 0.4 #set walk velocity
        self.Uy = 0.4
        self.Uz = 0.4
        self.Wrot = 0
        self.angle_FR = 0 #out put angle
        self.angle_FL = 0
        self.angle_BR = 0
        self.angle_BL = 0
        self.zeta_FR = 0 #set leg walk angle
        self.zeta_FL = 0
        self.zeta_BR = 0
        self.zeta_BL = 0
        self.step_offset = 0.75
        self.T = 1.6 #period of time (in seconds) of every step
        self.offset = np.array([0. , 0.5 , 0.5 , 0.]) 
        # Limb transformation params
        self.Foot_Position = np.asarray([[0, 0, 0], 
                                         [0, 0, 0], 
                                         [0, 0, 0], 
                                         [0, 0, 0]])
        # Body transformation params
        self.body_orientation = np.asarray([0, 0, 0])
        self.body_position = np.asarray([0., 0., 0.])
    
    def toggle_mode(self, X, square, triangle, circle):
        if X:
            if not self.mode["X"]:
                self.mode["X"] = True
                self.submode['l1'] = False
                self.submode['l2'] = False
                self.submode['r1'] = False
                self.submode['r2'] = False
                self.submode['pause'] = False
                self.submode['share'] = False
                self.subsubmode["up"] = False
                self.subsubmode["right"] = False
                self.subsubmode["down"] = False
                self.subsubmode["left"] = False
            self.mode["square"] = False
            self.mode["triangle"] = False
            self.mode["circle"] = False
        if square:
            if not self.mode["square"]:
                self.mode["square"] = True
                self.submode['l1'] = False
                self.submode['l2'] = False
                self.submode['r1'] = False
                self.submode['r2'] = False
                self.submode['pause'] = False
                self.submode['share'] = False
                self.subsubmode["up"] = False
                self.subsubmode["right"] = False
                self.subsubmode["down"] = False
                self.subsubmode["left"] = False
            self.mode["X"] = False
            self.mode["triangle"] = False
            self.mode["circle"] = False
        if triangle:
            if not self.mode["triangle"]:
                self.mode["triangle"] = True
                self.submode['l1'] = False
                self.submode['l2'] = False
                self.submode['r1'] = False
                self.submode['r2'] = False
                self.submode['pause'] = False
                self.submode['share'] = False
                self.subsubmode["up"] = False
                self.subsubmode["right"] = False
                self.subsubmode["down"] = False
                self.subsubmode["left"] = False
            self.mode["X"] = False
            self.mode["square"] = False
            self.mode["circle"] = False
        if circle:
            if not self.mode["circle"]:
                self.mode["circle"] = True
                self.submode['l1'] = False
                self.submode['l2'] = False
                self.submode['r1'] = False
                self.submode['r2'] = False
                self.submode['pause'] = False
                self.submode['share'] = False
                self.subsubmode["up"] = False
                self.subsubmode["right"] = False
                self.subsubmode["down"] = False
                self.subsubmode["left"] = False
            self.mode["X"] = False
            self.mode["square"] = False
            self.mode["triangle"] = False

    def toggle_submode(self, l1, l2, r1, r2, pause, share):
        if l1:
            if not self.submode['l1']:
                self.submode['l1'] = True
                self.subsubmode["up"] = False
                self.subsubmode["right"] = False
                self.subsubmode["down"] = False
                self.subsubmode["left"] = False
            self.submode['l2'] = False
            self.submode['r1'] = False
            self.submode['r2'] = False
        if l2:
            if not self.submode['l2']:
                self.submode['l2'] = True
                self.subsubmode["up"] = False
                self.subsubmode["right"] = False
                self.subsubmode["down"] = False
                self.subsubmode["left"] = False
            self.submode['l1'] = False
            self.submode['r1'] = False
            self.submode['r2'] = False
            self.submode['pause'] = False
            self.submode['share'] = False
        if r1:
            if not self.submode['r1']:
                self.submode['r1'] = True
                self.subsubmode["up"] = False
                self.subsubmode["right"] = False
                self.subsubmode["down"] = False
                self.subsubmode["left"] = False
            self.submode['l1'] = False
            self.submode['l2'] = False
            self.submode['r2'] = False
            self.submode['pause'] = False
            self.submode['share'] = False
        if r2:
            if not self.submode['r2']:
                self.submode['r2'] = True
                self.subsubmode["up"] = False
                self.subsubmode["right"] = False
                self.subsubmode["down"] = False
                self.subsubmode["left"] = False
            self.submode['l1'] = False
            self.submode['l2'] = False
            self.submode['r1'] = False
            self.submode['pause'] = False
            self.submode['share'] = False
        if pause:
            if not sself.submode['pause']:
                self.submode['pause'] = True
                self.subsubmode["up"] = False
                self.subsubmode["right"] = False
                self.subsubmode["down"] = False
                self.subsubmode["left"] = False
            self.submode['l1'] = False
            self.submode['l2'] = False
            self.submode['r1'] = False
            self.submode['r2'] = False
            self.submode['share'] = False
        if share:
            if not self.submode['share']:
                self.submode['share'] = True
                self.subsubmode["up"] = False
                self.subsubmode["right"] = False
                self.subsubmode["down"] = False
                self.subsubmode["left"] = False
            self.submode['l1'] = False
            self.submode['l2'] = False
            self.submode['r1'] = False
            self.submode['r2'] = False
            self.submode['pause'] = False

    def toggle_subsubmode(self, up, right, down, left):
        if up:
            if not self.subsubmode["up"]:
                self.subsubmode["up"] = True
            self.subsubmode["right"] = False
            self.subsubmode["down"] = False
            self.subsubmode["left"] = False
        if right:
            if not self.subsubmode["right"]:
                self.subsubmode["right"] = True
            self.subsubmode["up"] = False
            self.subsubmode["down"] = False
            self.subsubmode["left"] = False
        if down:
            if not self.subsubmode["down"]:
                self.subsubmode["down"] = True
            self.subsubmode["up"] = False
            self.subsubmode["right"] = False
            self.subsubmode["left"] = False
        if left:
            if not self.subsubmode["left"]:
                self.subsubmode["left"] = True
            self.subsubmode["up"] = False
            self.subsubmode["right"] = False
            self.subsubmode["down"] = False

    def adjust_params(self, mode, submode, subsubmode, button_state):
        if mode["X"]:
            if button_state['left_joystick']['active']:
                self.angle_FR = button_state['left_joystick']['angle']
                self.angle_FL = button_state['left_joystick']['angle']
                self.angle_BR = button_state['left_joystick']['angle']
                self.angle_BL = button_state['left_joystick']['angle']
                self.Vx = self.Ux
                self.Vy = self.Uy
                self.Vz = self.Uz
            elif button_state['right_joystick']['active']:
                if button_state['right_joystick']['x'] < 127:
                    if not self.wrot_status['left']:
                        self.wrot_status['left'] = True
                        self.Wrot += 0.1
                    self.wrot_status['right'] = False
                else: 
                    if not self.wrot_status['right']:
                        self.wrot_status['right'] = True
                        self.Wrot -= 0.1
                    self.wrot_status['left'] = False
            elif button_state['SELECT']:
                self.angle_FR = self.zeta_FR
                self.angle_FL = self.zeta_FL
                self.angle_BR = self.zeta_BR
                self.angle_BL = self.zeta_BL
                self.Vx = self.Ux
                self.Vy = self.Uy
                self.Vz = self.Uz
            else:
                self.angle_FR = 0
                self.angle_FL = 0
                self.angle_BR = 0
                self.angle_BL = 0
                self.Vx = 0
                self.Vy = 0
                self.Vz = 0
                self.wrot_status['right'] = False
                self.wrot_status['left'] = False
        elif mode["square"]:
            if submode['l1']:
                if subsubmode['up']:
                    if button_state['right_joystick']['active']:
                        if button_state['right_joystick']['x'] < 127:
                            if not self.idcrease['increase']:
                                self.idcrease['increase'] = True
                                self.Ux += 0.01
                            self.idcrease['decrease'] = False
                        else:
                            if not self.idcrease['decrease']:
                                self.idcrease['decrease'] = True
                                self.Ux -= 0.01
                            self.idcrease['increase'] = False
                    else:
                        self.idcrease['increase'] = False
                        self.idcrease['decrease'] = False         
                if subsubmode['right']:
                    if button_state['right_joystick']['active']:
                        if button_state['right_joystick']['x'] < 127:
                            if not self.idcrease['increase']:
                                self.idcrease['increase'] = True
                                self.Uy += 0.01
                            self.idcrease['decrease'] = False
                        else:
                            if not self.idcrease['decrease']:
                                self.idcrease['decrease'] = True
                                self.Uy -= 0.01
                            self.idcrease['increase'] = False
                    else:
                        self.idcrease['increase'] = False
                        self.idcrease['decrease'] = False    
                if subsubmode['down']:
                    if button_state['right_joystick']['active']:
                        if button_state['right_joystick']['x'] < 127:
                            if not self.idcrease['increase']:
                                self.idcrease['increase'] = True
                                self.Uz += 0.01
                            self.idcrease['decrease'] = False
                        else:
                            if not self.idcrease['decrease']:
                                self.idcrease['decrease'] = True
                                self.Uz -= 0.01
                            self.idcrease['increase'] = False
                    else:
                        self.idcrease['increase'] = False
                        self.idcrease['decrease'] = False    
                if subsubmode['left']:
                    if button_state['right_joystick']['active']:
                        if button_state['right_joystick']['x'] < 127:
                            if not self.idcrease['increase']:
                                self.idcrease['increase'] = True
                                self.Ux += 0.01
                                self.Uy += 0.01
                                self.Uz += 0.01
                            self.idcrease['decrease'] = False
                        else:
                            if not self.idcrease['decrease']:
                                self.idcrease['decrease'] = True
                                self.Ux -= 0.01
                                self.Uy -= 0.01
                                self.Uz -= 0.01
                            self.idcrease['increase'] = False
                    else:
                        self.idcrease['increase'] = False
                        self.idcrease['decrease'] = False    
            elif submode['l2']:
                if subsubmode['up']:
                    if button_state['right_joystick']['active']:
                        if button_state['right_joystick']['x'] < 127:
                            if not self.idcrease['increase']:
                                self.idcrease['increase'] = True
                                self.zeta_FR += 1
                            self.idcrease['decrease'] = False
                        else:
                            if not self.idcrease['decrease']:
                                self.idcrease['decrease'] = True
                                self.zeta_FR -= 1
                            self.idcrease['increase'] = False
                    else:
                        self.idcrease['increase'] = False
                        self.idcrease['decrease'] = False    
                if subsubmode['right']:
                    if button_state['right_joystick']['active']:
                        if button_state['right_joystick']['x'] < 127:
                            if not self.idcrease['increase']:
                                self.idcrease['increase'] = True
                                self.zeta_FL += 1
                            self.idcrease['decrease'] = False
                        else:
                            if not self.idcrease['decrease']:
                                self.idcrease['decrease'] = True
                                self.zeta_FL -= 1
                            self.idcrease['increase'] = False
                    else:
                        self.idcrease['increase'] = False
                        self.idcrease['decrease'] = False    
                if subsubmode['down']:
                    if button_state['right_joystick']['active']:
                        if button_state['right_joystick']['x'] < 127:
                            if not self.idcrease['increase']:
                                self.idcrease['increase'] = True
                                self.zeta_BR += 1
                            self.idcrease['decrease'] = False
                        else:
                            if not self.idcrease['decrease']:
                                self.idcrease['decrease'] = True
                                self.zeta_BR -= 1
                            self.idcrease['increase'] = False
                    else:
                        self.idcrease['increase'] = False
                        self.idcrease['decrease'] = False    
                if subsubmode['left']:
                    if button_state['right_joystick']['active']:
                        if button_state['right_joystick']['x'] < 127:
                            if not self.idcrease['increase']:
                                self.idcrease['increase'] = True
                                self.zeta_BL += 1
                            self.idcrease['decrease'] = False
                        else:
                            if not self.idcrease['decrease']:
                                self.idcrease['decrease'] = True
                                self.zeta_BL -= 1
                            self.idcrease['increase'] = False
                    else:
                        self.idcrease['increase'] = False
                        self.idcrease['decrease'] = False    
            elif submode['r1']:   
                if button_state['right_joystick']['active']:
                    if button_state['right_joystick']['x'] < 127:
                        if not self.idcrease['increase']:
                            self.idcrease['increase'] = True
                            self.T += 0.01
                        self.idcrease['decrease'] = False
                    else:
                        if not self.idcrease['decrease']:
                            self.idcrease['decrease'] = True
                            self.T -= 0.01
                        self.idcrease['increase'] = False      
                else:
                    self.idcrease['increase'] = False
                    self.idcrease['decrease'] = False           
            elif submode['r2']:
                if subsubmode['up']: #FR
                    if button_state['right_joystick']['active']:
                        if button_state['right_joystick']['x'] < 127:
                            if not self.idcrease['increase']:
                                self.idcrease['increase'] = True
                                self.offset[0] += 0.01
                            self.idcrease['decrease'] = False
                        else:
                            if not self.idcrease['decrease']:
                                self.idcrease['decrease'] = True
                                self.offset[0] -= 0.01
                            self.idcrease['increase'] = False
                    else:
                        self.idcrease['increase'] = False
                        self.idcrease['decrease'] = False    
                if subsubmode['right']: #FL
                    if button_state['right_joystick']['active']:
                        if button_state['right_joystick']['x'] < 127:
                            if not self.idcrease['increase']:
                                self.idcrease['increase'] = True
                                self.offset[1] += 0.01
                            self.idcrease['decrease'] = False
                        else:
                            if not self.idcrease['decrease']:
                                self.idcrease['decrease'] = True
                                self.offset[1] -= 0.01
                            self.idcrease['increase'] = False
                    else:
                        self.idcrease['increase'] = False
                        self.idcrease['decrease'] = False    
                if subsubmode['down']: #BR
                    if button_state['right_joystick']['active']:
                        if button_state['right_joystick']['x'] < 127:
                            if not self.idcrease['increase']:
                                self.idcrease['increase'] = True
                                self.offset[2] += 0.01
                            self.idcrease['decrease'] = False
                        else:
                            if not self.idcrease['decrease']:
                                self.idcrease['decrease'] = True
                                self.offset[2] -= 0.01
                            self.idcrease['increase'] = False
                    else:
                        self.idcrease['increase'] = False
                        self.idcrease['decrease'] = False    
                if subsubmode['left']: #BL
                    if button_state['right_joystick']['active']:
                        if button_state['right_joystick']['x'] < 127:
                            if not self.idcrease['increase']:
                                self.idcrease['increase'] = True
                                self.offset[3] += 0.01
                            self.idcrease['decrease'] = False
                        else:
                            if not self.idcrease['decrease']:
                                self.idcrease['decrease'] = True
                                self.offset[3] -= 0.01
                            self.idcrease['increase'] = False
                    else:
                        self.idcrease['increase'] = False
                        self.idcrease['decrease'] = False    
            elif submode['share']:
                if button_state['right_joystick']['active']:
                    if button_state['right_joystick']['x'] < 127:
                        if not self.idcrease['increase']:
                            self.idcrease['increase'] = True
                            self.step_offset += 0.01
                        self.idcrease['decrease'] = False
                    else:
                        if not self.idcrease['decrease']:
                            self.idcrease['decrease'] = True
                            self.step_offset -= 0.01
                        self.idcrease['increase'] = False   
                else:
                    self.idcrease['increase'] = False
                    self.idcrease['decrease'] = False      
            else:
                self.idcrease['increase'] = False
                self.idcrease['decrease'] = False        
        elif mode["triangle"]:
            if submode['l1']:
                if subsubmode['up']:
                    if button_state['right_joystick']['active']:
                        if button_state['right_joystick']['x'] < 127:
                            if not self.idcrease['increase']:
                                self.idcrease['increase'] = True
                                self.body_orientation[0] += 1
                            self.idcrease['decrease'] = False
                        else:
                            if not self.idcrease['decrease']:
                                self.idcrease['decrease'] = True
                                self.body_orientation[0] -= 1
                            self.idcrease['increase'] = False
                    else:
                        self.idcrease['increase'] = False
                        self.idcrease['decrease'] = False    
                if subsubmode['right']:
                    if button_state['right_joystick']['active']:
                        if button_state['right_joystick']['x'] < 127:
                            if not self.idcrease['increase']:
                                self.idcrease['increase'] = True
                                self.body_orientation[1] += 1
                            self.idcrease['decrease'] = False
                        else:
                            if not self.idcrease['decrease']:
                                self.idcrease['decrease'] = True
                                self.body_orientation[1] -= 1
                            self.idcrease['increase'] = False
                    else:
                        self.idcrease['increase'] = False
                        self.idcrease['decrease'] = False    
                if subsubmode['down']:
                    if button_state['right_joystick']['active']:
                        if button_state['right_joystick']['x'] < 127:
                            if not self.idcrease['increase']:
                                self.idcrease['increase'] = True
                                self.body_orientation[2] += 1
                            self.idcrease['decrease'] = False
                        else:
                            if not self.idcrease['decrease']:
                                self.idcrease['decrease'] = True
                                self.body_orientation[2] -= 1
                            self.idcrease['increase'] = False
                    else:
                        self.idcrease['increase'] = False
                        self.idcrease['decrease'] = False    
                if subsubmode['left']:
                    if button_state['right_joystick']['active']:
                        if button_state['right_joystick']['x'] < 127:
                            if not self.idcrease['increase']:
                                self.idcrease['increase'] = True
                                self.body_orientation[0] += 1
                                self.body_orientation[1] += 1
                                self.body_orientation[2] += 1
                            self.idcrease['decrease'] = False
                        else:
                            if not self.idcrease['decrease']:
                                self.idcrease['decrease'] = True
                                self.body_orientation[0] -= 1
                                self.body_orientation[1] -= 1
                                self.body_orientation[2] -= 1
                            self.idcrease['increase'] = False
                    else:
                        self.idcrease['increase'] = False
                        self.idcrease['decrease'] = False    
            elif submode['r1']:
                if subsubmode['up']:
                    if button_state['right_joystick']['active']:
                        if button_state['right_joystick']['x'] < 127:
                            if not self.idcrease['increase']:
                                self.idcrease['increase'] = True
                                self.body_position[0] += 0.01
                            self.idcrease['decrease'] = False
                        else:
                            if not self.idcrease['decrease']:
                                self.idcrease['decrease'] = True
                                self.body_position[0] -= 0.01
                                self.body_orientation[1] -= 1
                                self.body_orientation[2] -= 1
                            self.idcrease['increase'] = False
                    else:
                        self.idcrease['increase'] = False
                        self.idcrease['decrease'] = False    
                if subsubmode['right']:
                    if button_state['right_joystick']['active']:
                        if button_state['right_joystick']['x'] < 127:
                            if not self.idcrease['increase']:
                                self.idcrease['increase'] = True
                                self.body_position[1] += 0.01
                            self.idcrease['decrease'] = False
                        else:
                            if not self.idcrease['decrease']:
                                self.idcrease['decrease'] = True
                                self.body_position[1] -= 0.01
                            self.idcrease['increase'] = False
                    else:
                        self.idcrease['increase'] = False
                        self.idcrease['decrease'] = False    
                if subsubmode['down']:
                    if button_state['right_joystick']['active']:
                        if button_state['right_joystick']['x'] < 127:
                            if not self.idcrease['increase']:
                                self.idcrease['increase'] = True
                                self.body_position[2] += 0.01
                            self.idcrease['decrease'] = False
                        else:
                            if not self.idcrease['decrease']:
                                self.idcrease['decrease'] = True
                                self.body_position[2] -= 0.01
                            self.idcrease['increase'] = False
                    else:
                        self.idcrease['increase'] = False
                        self.idcrease['decrease'] = False    
                if subsubmode['left']:
                    if button_state['right_joystick']['active']:
                        if button_state['right_joystick']['x'] < 127:
                            if not self.idcrease['increase']:
                                self.idcrease['increase'] = True
                                self.body_position[0] += 0.01
                                self.body_position[1] += 0.01
                                self.body_position[2] += 0.01
                            self.idcrease['decrease'] = False
                        else:
                            if not self.idcrease['decrease']:
                                self.idcrease['decrease'] = True
                                self.body_position[0] -= 0.01
                                self.body_position[1] -= 0.01
                                self.body_position[2] -= 0.01
                            self.idcrease['increase'] = False
                    else:
                        self.idcrease['increase'] = False
                        self.idcrease['decrease'] = False    
            else:
                self.idcrease['increase'] = False
                self.idcrease['decrease'] = False
        elif mode["circle"]:
            if submode['r1']:
                if subsubmode['up']:
                    if button_state['right_joystick']['active']:
                        if button_state['right_joystick']['x'] < 127:
                            if not self.idcrease['increase']:
                                self.idcrease['increase'] = True
                                self.Foot_Position[0][0] += 0.01
                            self.idcrease['decrease'] = False
                        else:
                            if not self.idcrease['decrease']:
                                self.idcrease['decrease'] = True
                                self.Foot_Position[0][0] -= 0.01
                            self.idcrease['increase'] = False
                    else:
                        self.idcrease['increase'] = False
                        self.idcrease['decrease'] = False    
                if subsubmode['right']:
                    if button_state['right_joystick']['active']:
                        if button_state['right_joystick']['x'] < 127:
                            if not self.idcrease['increase']:
                                self.idcrease['increase'] = True
                                self.Foot_Position[0][1] += 0.01
                            self.idcrease['decrease'] = False
                        else:
                            if not self.idcrease['decrease']:
                                self.idcrease['decrease'] = True
                                self.Foot_Position[0][1] -= 0.01
                            self.idcrease['increase'] = False
                    else:
                        self.idcrease['increase'] = False
                        self.idcrease['decrease'] = False    
                if subsubmode['down']:
                    if button_state['right_joystick']['active']:
                        if button_state['right_joystick']['x'] < 127:
                            if not self.idcrease['increase']:
                                self.idcrease['increase'] = True
                                self.Foot_Position[0][2] += 0.01
                            self.idcrease['decrease'] = False
                        else:
                            if not self.idcrease['decrease']:
                                self.idcrease['decrease'] = True
                                self.Foot_Position[0][2] -= 0.01
                            self.idcrease['increase'] = False
                    else:
                        self.idcrease['increase'] = False
                        self.idcrease['decrease'] = False    
                if subsubmode['left']:
                    if button_state['right_joystick']['active']:
                        if button_state['right_joystick']['x'] < 127:
                            if not self.idcrease['increase']:
                                self.idcrease['increase'] = True
                                self.Foot_Position[0][0] += 0.01
                                self.Foot_Position[0][1] += 0.01
                                self.Foot_Position[0][2] += 0.01
                            self.idcrease['decrease'] = False
                        else:
                            if not self.idcrease['decrease']:
                                self.idcrease['decrease'] = True
                                self.Foot_Position[0][0] -= 0.01
                                self.Foot_Position[0][1] -= 0.01
                                self.Foot_Position[0][2] -= 0.01
                            self.idcrease['increase'] = False
                    else:
                        self.idcrease['increase'] = False
                        self.idcrease['decrease'] = False    
            elif submode['l1']:
                if subsubmode['up']:
                    if button_state['right_joystick']['active']:
                        if button_state['right_joystick']['x'] < 127:
                            if not self.idcrease['increase']:
                                self.idcrease['increase'] = True
                                self.Foot_Position[1][0] += 0.01
                            self.idcrease['decrease'] = False
                        else:
                            if not self.idcrease['decrease']:
                                self.idcrease['decrease'] = True
                                self.Foot_Position[1][0] -= 0.01
                            self.idcrease['increase'] = False
                    else:
                        self.idcrease['increase'] = False
                        self.idcrease['decrease'] = False    
                if subsubmode['right']:
                    if button_state['right_joystick']['active']:
                        if button_state['right_joystick']['x'] < 127:
                            if not self.idcrease['increase']:
                                self.idcrease['increase'] = True
                                self.Foot_Position[1][1] += 0.01
                            self.idcrease['decrease'] = False
                        else:
                            if not self.idcrease['decrease']:
                                self.idcrease['decrease'] = True
                                self.Foot_Position[1][1] -= 0.01
                            self.idcrease['increase'] = False
                    else:
                        self.idcrease['increase'] = False
                        self.idcrease['decrease'] = False    
                if subsubmode['down']:
                    if button_state['right_joystick']['active']:
                        if button_state['right_joystick']['x'] < 127:
                            if not self.idcrease['increase']:
                                self.idcrease['increase'] = True
                                self.Foot_Position[1][2] += 0.01
                            self.idcrease['decrease'] = False
                        else:
                            if not self.idcrease['decrease']:
                                self.idcrease['decrease'] = True
                                self.Foot_Position[1][2] -= 0.01
                            self.idcrease['increase'] = False
                    else:
                        self.idcrease['increase'] = False
                        self.idcrease['decrease'] = False    
                if subsubmode['left']:
                    if button_state['right_joystick']['active']:
                        if button_state['right_joystick']['x'] < 127:
                            if not self.idcrease['increase']:
                                self.idcrease['increase'] = True
                                self.Foot_Position[1][0] += 0.01
                                self.Foot_Position[1][1] += 0.01
                                self.Foot_Position[1][2] += 0.01
                            self.idcrease['decrease'] = False
                        else:
                            if not self.idcrease['decrease']:
                                self.idcrease['decrease'] = True
                                self.Foot_Position[1][0] -= 0.01
                                self.Foot_Position[1][1] -= 0.01
                                self.Foot_Position[1][2] -= 0.01
                            self.idcrease['increase'] = False
                    else:
                        self.idcrease['increase'] = False
                        self.idcrease['decrease'] = False    
            elif submode['r2']:   
                if subsubmode['up']:
                    if button_state['right_joystick']['active']:
                        if button_state['right_joystick']['x'] < 127:
                            if not self.idcrease['increase']:
                                self.idcrease['increase'] = True
                                self.Foot_Position[2][0] += 0.01
                            self.idcrease['decrease'] = False
                        else:
                            if not self.idcrease['decrease']:
                                self.idcrease['decrease'] = True
                                self.Foot_Position[2][0] -= 0.01
                            self.idcrease['increase'] = False
                    else:
                        self.idcrease['increase'] = False
                        self.idcrease['decrease'] = False    
                if subsubmode['right']:
                    if button_state['right_joystick']['active']:
                        if button_state['right_joystick']['x'] < 127:
                            if not self.idcrease['increase']:
                                self.idcrease['increase'] = True
                                self.Foot_Position[2][1] += 0.01
                            self.idcrease['decrease'] = False
                        else:
                            if not self.idcrease['decrease']:
                                self.idcrease['decrease'] = True
                                self.Foot_Position[2][1] -= 0.01
                            self.idcrease['increase'] = False
                    else:
                        self.idcrease['increase'] = False
                        self.idcrease['decrease'] = False    
                if subsubmode['down']:
                    if button_state['right_joystick']['active']:
                        if button_state['right_joystick']['x'] < 127:
                            if not self.idcrease['increase']:
                                self.idcrease['increase'] = True
                                self.Foot_Position[2][2] += 0.01
                            self.idcrease['decrease'] = False
                        else:
                            if not self.idcrease['decrease']:
                                self.idcrease['decrease'] = True
                                self.Foot_Position[2][2] -= 0.01
                            self.idcrease['increase'] = False
                    else:
                        self.idcrease['increase'] = False
                        self.idcrease['decrease'] = False    
                if subsubmode['left']:
                    if button_state['right_joystick']['active']:
                        if button_state['right_joystick']['x'] < 127:
                            if not self.idcrease['increase']:
                                self.idcrease['increase'] = True
                                self.Foot_Position[2][0] += 0.01
                                self.Foot_Position[2][1] += 0.01
                                self.Foot_Position[2][2] += 0.01
                            self.idcrease['decrease'] = False
                        else:
                            if not self.idcrease['decrease']:
                                self.idcrease['decrease'] = True
                                self.Foot_Position[2][0] -= 0.01
                                self.Foot_Position[2][1] -= 0.01
                                self.Foot_Position[2][2] -= 0.01
                            self.idcrease['increase'] = False   
                    else:
                        self.idcrease['increase'] = False
                        self.idcrease['decrease'] = False        
            elif submode['l2']:
                if subsubmode['up']:
                    if button_state['right_joystick']['active']:
                        if button_state['right_joystick']['x'] < 127:
                            if not self.idcrease['increase']:
                                self.idcrease['increase'] = True
                                self.Foot_Position[3][0] += 0.01
                            self.idcrease['decrease'] = False
                        else:
                            if not self.idcrease['decrease']:
                                self.idcrease['decrease'] = True
                                self.Foot_Position[3][0] -= 0.01
                            self.idcrease['increase'] = False
                    else:
                        self.idcrease['increase'] = False
                        self.idcrease['decrease'] = False    
                if subsubmode['right']:
                    if button_state['right_joystick']['active']:
                        if button_state['right_joystick']['x'] < 127:
                            if not self.idcrease['increase']:
                                self.idcrease['increase'] = True
                                self.Foot_Position[3][1] += 0.01
                            self.idcrease['decrease'] = False
                        else:
                            if not self.idcrease['decrease']:
                                self.idcrease['decrease'] = True
                                self.Foot_Position[3][1] -= 0.01
                            self.idcrease['increase'] = False
                    else:
                        self.idcrease['increase'] = False
                        self.idcrease['decrease'] = False    
                if subsubmode['down']:
                    if button_state['right_joystick']['active']:
                        if button_state['right_joystick']['x'] < 127:
                            if not self.idcrease['increase']:
                                self.idcrease['increase'] = True
                                self.Foot_Position[3][2] += 0.01
                            self.idcrease['decrease'] = False
                        else:
                            if not self.idcrease['decrease']:
                                self.idcrease['decrease'] = True
                                self.Foot_Position[3][2] -= 0.01
                            self.idcrease['increase'] = False
                    else:
                        self.idcrease['increase'] = False
                        self.idcrease['decrease'] = False    
                if subsubmode['left']:
                    if button_state['right_joystick']['active']:
                        if button_state['right_joystick']['x'] < 127:
                            if not self.idcrease['increase']:
                                self.idcrease['increase'] = True
                                self.Foot_Position[3][0] += 0.01
                                self.Foot_Position[3][1] += 0.01
                                self.Foot_Position[3][2] += 0.01
                            self.idcrease['decrease'] = False
                        else:
                            if not self.idcrease['decrease']:
                                self.idcrease['decrease'] = True
                                self.Foot_Position[3][0] -= 0.01
                                self.Foot_Position[3][1] -= 0.01
                                self.Foot_Position[3][2] -= 0.01
                            self.idcrease['increase'] = False
                    else:
                        self.idcrease['increase'] = False
                        self.idcrease['decrease'] = False    
            else:
                self.idcrease['increase'] = False
                self.idcrease['decrease'] = False

    def print_params(self):
        print("Vx:", self.Vx)
        print("Vy:", self.Vy)
        print("Vz:", self.Vz)
        print("Ux:", self.Ux)
        print("Uy:", self.Uy)
        print("Uz:", self.Uz)
        print("Wrot:", self.Wrot)
        print("angle_FR:", self.angle_FR)
        print("angle_FL:", self.angle_FL)
        print("angle_BR:", self.angle_BR)
        print("angle_BL:", self.angle_BL)
        print("zeta_FR:", self.zeta_FR)
        print("zeta_FL:", self.zeta_FL)
        print("zeta_BR:", self.zeta_BR)
        print("zeta_BL:", self.zeta_BL)
        print("step_offset:", self.step_offset)
        print("T:", self.T)
        print("offset:", self.offset)
        print("Foot_Position:", self.Foot_Position)
        print("body_orientation:", self.body_orientation)
        print("body_position:", self.body_position)
        print("mode:", self.mode)
        print("mode:", self.submode)
        print("mode:", self.subsubmode)
        print(self.idcrease)

    def read_events(self):
        for event in self.gamepad.read_loop():
            if event.type == ecodes.EV_KEY:
                self.buttons_state.handle_button_press(event)
            elif event.type == ecodes.EV_ABS:
                self.buttons_state.handle_joystick(event)
                self.buttons_state.handle_dpad(event)
            self.controller_state = self.buttons_state.get_button_states()|self.buttons_state.get_dpad_states()|self.buttons_state.get_joystick_states()
            self.toggle_mode(self.controller_state['X'], self.controller_state['SQUARE'], self.controller_state['TRIANGLE'], self.controller_state['CIRCLE'])
            self.toggle_submode(self.controller_state['L1'], self.controller_state['L2'], self.controller_state['R1'], self.controller_state['R2'], self.controller_state['START'], self.controller_state['SELECT'])
            self.toggle_subsubmode(self.controller_state['UP'], self.controller_state['RIGHT'], self.controller_state['DOWN'], self.controller_state['LEFT'])
            self.adjust_params(self.mode, self.submode, self.subsubmode, self.controller_state)
            self.print_params()


if __name__ == "__main__":
    controller = QuadrupedController('/dev/input/event1')  # Adjust to your gamepad device
    controller.read_events()
    

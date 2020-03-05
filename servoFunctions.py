#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Pigpio library must be initialized.
    
    To check if already initialized, write the following in terminal: 
        pigs t
        
    if not initialized, start daemon by writing the following in terminal: 
        sudo pigpiod
        
    pigpio uses GPIO pins on RPi!
        
    """
import pigpio

class servoFunctions(object):
    
    def __init__(self, pin1, pin2, pin3, pin4):
        self.pin1 = pin1
        self.pin2 = pin2
        self.pin3 = pin3
        self.pin4 = pin4
        
        self.pi = pigpio.pi()
        
        if self.pin1 != 0:
            self.pi.set_mode(self.pin1, pigpio.OUTPUT)
            self.servo1Angle = 90
            self.servo1MaxAngle = 180
            self.servo1MinAngle = 0
         
        if self.pin2 != 0:
            self.pi.set_mode(self.pin2, pigpio.OUTPUT)
            self.servo2Angle = 90
            self.servo2MaxAngle = 125
            self.servo2MinAngle = 85

        if self.pin3 != 0:
            self.pi.set_mode(self.pin3, pigpio.OUTPUT)
            self.servo3Angle = 90
            self.servo3MaxAngle = 125
            self.servo3MinAngle = 85

        if self.pin4 != 0:
            self.pi.set_mode(self.pin4, pigpio.OUTPUT)
            self.servo4Angle = 90
            self.servo4MaxAngle = 125
            self.servo4MinAngle = 85
            
        self.UpdateAngles()
            
            
    def AdjustServoAngleByValue(self, servo, value):
        if servo == 1:
            self.servo1Angle += value
            angle = self.servo1Angle
        if servo == 2:
            self.servo2Angle += value
            angle = self.servo2Angle
        if servo == 3:
            self.servo3Angle += value
            angle = self.servo3Angle
        if servo == 4:
            self.servo4Angle += value
            angle = self.servo4Angle
            
        self.SetServoAngle(angle, servo)
            
        
    def SetServoAngle(self, a, servo):
        if servo == 1:
            pin = self.pin1
            if a > self.servo1MaxAngle:
                angle = self.servo1MaxAngle
            elif a < self.servo1MinAngle:
                angle = self.servo1MinAngle
            else:
                angle = a
        if servo == 2:
            pin = self.pin2
            if a > self.servo2MaxAngle:
                angle = self.servo2MaxAngle
            elif a < self.servo2MinAngle:
                angle = self.servo2MinAngle
            else:
                angle = a
        if servo == 3:
            pin = self.pin3
            if a > self.servo3MaxAngle:
                angle = self.servo3MaxAngle
            elif a < self.servo3MinAngle:
                angle = self.servo3MinAngle
            else:
                angle = a
        if servo == 4:
            pin = self.pin4
            if a > self.servo4MaxAngle:
                angle = self.servo4MaxAngle
            elif a < self.servo4MinAngle:
                angle = self.servo4MinAngle
            else:
                angle = a


        pulsewidth = (angle * 11.1111) + 500
        print(angle)
        print(pulsewidth)
        
        self.pi.set_servo_pulsewidth(pin, pulsewidth)
        self.UpdateAngles()


    def UpdateAngles(self):
        pass
#        if hasattr(self, "servo1Angle"):
#            self.servo1Angle = self.pi.get_servo_pulsewidth(self.pin1)
#        if hasattr(self, "servo2Angle"):
#            self.servo2Angle = self.pi.get_servo_pulsewidth(self.pin2)
#        if hasattr(self, "servo3Angle"):
#            self.servo3Angle = self.pi.get_servo_pulsewidth(self.pin3)
#        if hasattr(self, "servo4Angle"):
#            self.servo4Angle = self.pi.get_servo_pulsewidth(self.pin4)
        
        
    def StopPigpio(self):
        self.pi.stop()

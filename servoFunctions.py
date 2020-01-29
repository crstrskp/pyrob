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
         
        if self.pin2 != 0:
            self.pi.set_mode(self.pin2, pigpio.OUTPUT)

        if self.pin3 != 0:
            self.pi.set_mode(self.pin3, pigpio.OUTPUT)

        if self.pin4 != 0:
            self.pi.set_mode(self.pin4, pigpio.OUTPUT)
            
    def SetServoAngle(self, angle, servo):
        
        pulsewidth = (angle * 11.1111) + 500

        if servo == 1:
            pin = self.pin1
        if servo == 2:
            pin = self.pin2
        if servo == 3:
            pin = self.pin3
        if servo == 4:
            pin = self.pin4
            
        self.pi.set_servo_pulsewidth(pin, pulsewidth)

    def StopPigpio(self):
        self.pi.stop()
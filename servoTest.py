#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 11:42:35 2020

@author: luffe
"""

import servoFunctions as servo
from time import sleep

sf = servo.servoFunctions(2, 3, 0, 0) # Uses GPIO pins!!

try: 
    while True:
        sf.SetServoAngle(0, 1)
        sleep(1)
        sf.SetServoAngle(45, 1)
        sleep(1)
        sf.SetServoAngle(90, 1)
        sleep(1)
        sf.SetServoAngle(135, 1)
        sleep(1)
        sf.SetServoAngle(180, 1)
        sleep(1)
        sf.SetServoAngle(135, 1)
        sleep(1)
        sf.SetServoAngle(90, 1)
        sleep(1)
        sf.SetServoAngle(45, 1)
        sleep(1)
except KeyboardInterrupt:
    sf.StopPigpio()

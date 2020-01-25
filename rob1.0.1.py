import time
import controllerPS4 as cont
import RPi.GPIO as GPIO
 
class rob(object):
    print('Initializing rob1.0.1...')
 
    myCont = cont.controllerPS4()
    myCont.update_inputs()
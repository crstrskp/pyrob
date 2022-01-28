import RPi.GPIO as GPIO
import pygame

pygame.init


 
class motorfunctions(object):
 
    def __init__(self, Pin1A, Pin1B, Pin2A, Pin2B):
        self.Motor1A = Pin1A
        self.Motor1B = Pin1B
 
        self.Motor2A = Pin2A
        self.Motor2B = Pin2B
 
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.Motor1A,GPIO.OUT)
        GPIO.setup(self.Motor1B,GPIO.OUT)
 
        GPIO.setup(self.Motor2A,GPIO.OUT)
        GPIO.setup(self.Motor2B,GPIO.OUT)
        
        GPIO.setup(15,GPIO.OUT) // Brushless DC
 
    
    def leftForward(self):
        print("leftForward method called.")
        GPIO.output(self.Motor1A,GPIO.HIGH)
        GPIO.output(self.Motor1B,GPIO.LOW)
 
    def rightForward(self):
        print("rightForward method called.")
        GPIO.output(self.Motor2A,GPIO.HIGH)
        GPIO.output(self.Motor2B,GPIO.LOW)
 
    def leftBackward(self):
        print("leftBackward method called.")
        GPIO.output(self.Motor1A,GPIO.LOW)
        GPIO.output(self.Motor1B,GPIO.HIGH)
 
    def rightBackward(self):
        print("rightBackward method called.")
        GPIO.output(self.Motor2A,GPIO.LOW)
        GPIO.output(self.Motor2B,GPIO.HIGH)
 
    def leftStop(self):
        print("leftStop method called.")
        GPIO.output(self.Motor1A,GPIO.LOW)
        GPIO.output(self.Motor1B,GPIO.LOW)
 
    def rightStop(self):
        print("rightStop method called.")
        GPIO.output(self.Motor2A,GPIO.LOW)
        GPIO.output(self.Motor2B,GPIO.LOW)
    
    
 
    def shutdown(self):
        print("shutting down...")
        GPIO.cleanup()

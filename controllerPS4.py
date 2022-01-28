import pygame
import RPi.GPIO as GPIO
import motorfunctions as m
import servoFunctions as s
import time
import pigpio

class controllerPS4(object):

    def saw(self):
        print("r2 clicked")
        
        ss = self.j.get_axis(5)

        const = ((ss+1)/2)

        
        if const > 0.999:
            const = 1

        speed = const*1000+1000
        self.pi.set_servo_pulsewidth(self.SAW, speed)
            
        if speed == 1000:
            self.pi.set_servo_pulsewidth(self.SAW, 1000)
        print(speed)  

    def beep(self):
        print("X!");
        if self.btnCount == 0:
            GPIO.output(15, GPIO.HIGH);
            self.btnCount = 1;  
        elif self.btnCount > 0:
            GPIO.output(15, GPIO.LOW);
            self.btnCount = 0;
    
    def __init__(self):
        self.btnCount = 0;
        print("ps4 controller setting enabled")
        
        // brushless DC: 
        self.SAW = 4
        self.pi = pigpio.pi()
        print("Set min value moter")
        self.pi.set_servo_pulsewidth(self.SAW, 1000)

        time.sleep(1)
        print("Set max value moter")
        self.pi.set_servo_pulsewidth(self.SAW, 2000)
        time.sleep(1)
        print("moter configured")

    def resetPyGameAndJoystick(self):
        pygame.quit()
        pygame.init()
        pygame.joystick.quit()
        pygame.joystick.init()


    def getController(self):
        self.resetPyGameAndJoystick()


        joystick_count = pygame.joystick.get_count()
        print(joystick_count)
        if joystick_count > 0:
            print("Controller found.")
            return pygame.joystick.Joystick(pygame.joystick.get_count()-1)
        else:
            print("could not find controller. Retrying in 3 seconds...")
            time.sleep(3)
            return self.getController()

    def SetupPygameAndController(self):
        try:
            self.resetPyGameAndJoystick()

            self.joystick_count = pygame.joystick.get_count()
            print("Joystick count: {0}".format(self.joystick_count))
            self.j = pygame.joystick.Joystick(pygame.joystick.get_count()-1)
            self.j.init()
            name = self.j.get_name()
            print("Joystick name: {}".format(name))
        except pygame.error:
            print("Joystick not found.")
            time.sleep(3)


    def update_inputs(self):

        #joystick_count = pygame.joystick.get_count()
        #print("Joystick count: {0}".format(joystick_count))
        #j = pygame.joystick.Joystick(pygame.joystick.get_count()-1)
        #j.init()
        #name = j.get_name()
        #print("Joystick name: {}".format(name))
        #pygame.init()
        #driveLeft = False
        #driveRight = False

        mf = m.motorfunctions(16, 18, 13, 11)
        sf = s.servoFunctions(2, 3, 0, 0)

        self.SetupPygameAndController()
        driveLeft = False
        driveRight = False

        try:
            print("Listening for inputs...")

            while True:

                if self.joystick_count < 1:

                    self.SetupPygameAndController()
                else:
                    for event in pygame.event.get():
                        if event.type == pygame.JOYAXISMOTION:
                            if self.j.get_axis(1):
                                left = self.j.get_axis(1)
                                if left < -0.9: # go forward left side
                                    if driveLeft == False:
                                        mf.leftForward()
                                        driveLeft = True
                                elif left > 0.9: # go backwards left side
                                    if driveLeft == False:
                                        mf.leftBackward()
                                        driveLeft = True
                            else:
                                if driveLeft:
                                    mf.leftStop()
                                    driveLeft = False

                            if self.j.get_axis(4):
                                right = self.j.get_axis(4)
                                if right < -0.9:
                                    if driveRight == False:
                                        mf.rightForward()
                                        driveRight = True
                                elif right > 0.9:
                                    if driveRight == False:
                                        mf.rightBackward()
                                        driveRight = True
                            else:
                                if driveRight:
                                    mf.rightStop()
                                    driveRight = False
                            if self.j.get_axis(5):
                                self.saw()

                        if event.type == pygame.JOYBUTTONDOWN:
                            if self.j.get_button(0):
                                self.beep()
                            

                    """ if event.type == pygame.JOYHATMOTION:
                            x, y = self.j.get_hat(0)
                            if x > 0:
                                print("right button clicked!")
                                sf.AdjustServoAngleByValue(1, 1) # first parameter refers to the first servo you set during init of sf.

                            if x < 0:
                                print("left button clicked!")
                                sf.AdjustServoAngleByValue(1, -1) # first parameter refers to the first servo you set during init of sf.
                            if y > 0:
                                print("up button clicked!")
                                sf.AdjustServoAngleByValue(2, 1) # first parameter refers to the first servo you set during init of sf.

                            if y < 0:
                                print("down button clicked!")
                                sf.AdjustServoAngleByValue(2, -1) # first parameter refers to the first servo you set during init of sf.
"""
        except KeyboardInterrupt:
            print("EXITING NOW")
            mf.shutdown()
            self.j.quit()

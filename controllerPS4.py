import pygame
import motorfunctions as m
import servoFunctions as s
import time



class controllerPS4(object):
 
   

    def __init__(self):
        print("ps4 controller setting enabled")
 
    def getController(self):
        print(".")
        pygame.quit()
        pygame.init()
        pygame.joystick.quit()
        pygame.joystick.init()
 
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
            pygame.init()
            pygame.joystick.quit()
 
            pygame.joystick.init();
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
                       
                     
                        if event.type == pygame.JOYBUTTONDOWN:
                            if self.j.get_button(0):
                                print("sag")
                                mf.SetAngle(120)
                                time.sleep(0.1)
                                mf.SetAngle(35)
                                
                        if event.type == pygame.JOYHATMOTION:
                            self.j.get_hat(0) => x, y
                                if x > 0:
                                    print("some hat pressed")
                                    sf.AdjustServoAngleByValue(1, 1) # first parameter refers to the first servo you set during init of sf.
                                if x < 0:
                                    print("some hat pressed")
                                    sf.AdjustServoAngleByValue(1, -1)
                                if y > 0:
                                    print("some hat pressed")
                                    sf.AdjustServoAngleByValue(2, 1)
                                if y < 0:
                                    print("some hat pressed")
                                    sf.AdjustServoAngleByValue(2, -1)

                            
                    
                           
        except KeyboardInterrupt:
            print("EXITING NOW")
            mf.shutdown()
            self.j.quit()
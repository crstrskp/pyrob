import time
import itertools

import pigpio  # http://abyz.me.uk/rpi/pigpio/python.html


class stepper:
    """
    A class to pulse a stepper.
    """

    def __init__(self, pi, g1, g2, g3, g4):

        self.pi = pi
        self.g1 = g1
        self.g2 = g2
        self.g3 = g3
        self.g4 = g4

        self.all = (1 << g1 | 1 << g2 | 1 << g3 | 1 << g4)

        self.pos = 0

        pi.set_mode(g1, pigpio.OUTPUT)
        pi.set_mode(g2, pigpio.OUTPUT)
        pi.set_mode(g3, pigpio.OUTPUT)
        pi.set_mode(g4, pigpio.OUTPUT)

    def move(self):
        pos = self.pos
        if pos < 0:
            pos = 7
        elif pos > 7:
            pos = 0
        self.pos = pos

        if pos == 0:
            on = (1 << self.g4)
        elif pos == 1:
            on = (1 << self.g3 | 1 << self.g4)
        elif pos == 2:
            on = (1 << self.g3)
        elif pos == 3:
            on = (1 << self.g2 | 1 << self.g3)
        elif pos == 4:
            on = (1 << self.g2)
        elif pos == 5:
            on = (1 << self.g1 | 1 << self.g2)
        elif pos == 6:
            on = (1 << self.g1)
        else:
            on = (1 << self.g1 | 1 << self.g4)

        off = on ^ self.all

        self.pi.clear_bank_1(off)
        self.pi.set_bank_1(on)

    def forward(self):
        self.pos += 1
        self.move()

    def backward(self):
        self.pos -= 1
        self.move()

    def stop(self):
        self.pi.clear_bank_1(self.all)


# Permutes the gpio assignments to find ones which successfully
# drive a stepper.  The stepper should move clockwise then
# anti-clockwise for DELAY seconds.

DELAY = 3

gpios = [27, 17, 22, 18]  # Set the gpios being used here.

pi = pigpio.pi()

if not pi.connected:
    exit(0)
#
# try:
#    for x in itertools.permutations(gpios):
#
s = stepper(pi, gpios[0], gpios[1], gpios[2], gpios[3])
#
#       print("Trying {}".format(x))
#
# stop = time.time() + DELAY
# while time.time() < stop:
while True:
    s.forward()
    time.sleep(0.0009)
    # best 0.0009
#
#       stop = time.time() + DELAY
#       while time.time() < stop:
#          s.backward()
#          time.sleep(0.0001)

# except KeyboardInterrupt:
#    pass

# s.stop()

pi.stop()
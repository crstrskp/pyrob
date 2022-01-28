import time

import pigpio

SERVO = 4

pi = pigpio.pi() # Connect to local Pi.

#print("min throttle")
pi.set_servo_pulsewidth(SERVO, 1000) # Minimum throttle.

time.sleep(1)

#print("max throttle")
pi.set_servo_pulsewidth(SERVO, 2000) # Maximum throttle.

time.sleep(1)

print("running")
for i in range(1100, 2000):
	print(i)
	pi.set_servo_pulsewidth(SERVO, i) # Slightly open throttle.
	time.sleep(0.025)

pi.set_servo_pulsewidth(SERVO, 0) # Stop servo pulses.

pi.stop() # Disconnect from local Raspberry Pi.


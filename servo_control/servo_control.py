from time import sleep
import pigpio

pi = pigpio.pi()

while True:

    pi.set_servo_pulsewidth(12, 0)    # off
    sleep(1)
    pi.set_servo_pulsewidth(12, 550) # position anti-clockwise
    sleep(1)
    pi.set_servo_pulsewidth(12, 1425) # middle
    sleep(1)
    pi.set_servo_pulsewidth(12, 2300) # position clockwise
    sleep(1)
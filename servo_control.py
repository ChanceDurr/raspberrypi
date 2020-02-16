import gpiozero
from gpiozero import Servo
from time import sleep
from gpiozero.tools import sin_values
import RPi.GPIO as GPIO

# GPIO.cleanup()
# GPIO.setmode(GPIO.BOARD)
# GPIO.setwarnings(False)

# GPIO.setup(11, GPIO.OUT)
# servo = GPIO.PWM(11, 50)

# servo.start(0)
# sleep(2)

# duty = 0

# while duty <= 12:
#     servo.ChangeDutyCycle(duty)
#     sleep(1)
#     duty += 1

# sleep(2)

# servo.ChangeDutyCycle(7)

# sleep(2)

# servo.ChangeDutyCycle(2)
# sleep(.5)
# servo.ChangeDutyCycle(0)

# servo.stop()
# GPIO.cleanup()

#####################

myGPIO=12
 
myCorrection=0.45
maxPW=(2.0+myCorrection)/1000
minPW=(1.0-myCorrection)/1000
 
servo = Servo(myGPIO,min_pulse_width=minPW,max_pulse_width=maxPW)
 
while True:
    servo.mid()
    print("mid")
    sleep(0.5)
    servo.min()
    print("min")
    sleep(1)
    servo.mid()
    print("mid")
    sleep(0.5)
    servo.max()
    print("max")
    sleep(1)

###############

# servo = Servo(12)

# servo.source = sin_values()
# servo.source_delay = 0.1
from machine import Pin, PWM
import time

# configure servo on pin G7 using PWM:
servo = PWM(Pin(7))
# configure PWM frequency:
servo.freq(50)

while(True):
    # move servo clockwise by chaning PWM duty:
    servo.duty(26)
    time.sleep(1)
    # move servo counterclockwise by changing PWM duty:
    servo.duty(123)
    time.sleep(1)


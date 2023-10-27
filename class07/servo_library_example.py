# controlling a servo using servo library
# servo.py library file should be burned on AtomS3 board

from servo import Servo
import time

# configure servo on pin G7:
servo = Servo(pin=7)

while(True):
    servo.move(85)  # move slowly clockwise
    time.sleep_ms(500)  
    servo.move(90)  # stop
    time.sleep(2)
    servo.move(100) # move slowly counter-clockwise
    time.sleep(1)

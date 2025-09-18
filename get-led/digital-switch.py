import RPi.GPIO as GPIO
import time
button = 13
state = 0
GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN)
while True:
    if GPIO.input(button):
        state = abs(state-1)
        GPIO.output(led,state)
        time.sleep(0.2)

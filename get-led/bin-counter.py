import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

leds = [24, 22, 23, 27, 17, 25, 12, 16]

GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)
light_time = 0.2
num = 0

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

up = 9
down = 10

GPIO.setup(up, GPIO.IN)
GPIO.setup(down, GPIO.IN)


while True:
    if GPIO.input(up):
        num = num + 1
        print(num, dec2bin(num))
    elif GPIO.input(down):
        num = num - 1
        print(num, dec2bin(num))

    dec = dec2bin(num)
    for i in range(8):
        if dec[i]:
            GPIO.output(leds[i], 1)
        else:
            GPIO.output(leds[i], 0)

    time.sleep(light_time)

import RPi.GPIO as GPIO
import time

led = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)


while True:
    GPIO.output(led, 1)
    time.sleep(0.2)
    GPIO.output(led, 0)
    time.sleep(0.2)

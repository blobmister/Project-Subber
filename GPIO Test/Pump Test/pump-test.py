import RPi.GPIO as GPIO
import time

m1in1 = 11
m1in2 = 13
m2in3 = 15
m2in4 = 16

GPIO.setmode(GPIO.BOARD)

GPIO.setup(m1in1, GPIO.OUT)
GPIO.setup(m1in2, GPIO.OUT)
GPIO.setup(m2in3, GPIO.OUT)
GPIO.setup(m2in4, GPIO.OUT)


def motorForward(num):
	if (num == 1):
		GPIO.output(m1in1, 1)
		GPIO.output(m1in2, 0)
	elif (num == 2):
		GPIO.output(m2in3 , 1)
		GPIO.output(m2in4, 0)
		
def motorOff(num):
	if (num == 1):
		GPIO.output(m1in1, 0)
		GPIO.output(m1in2, 0)
	elif (num == 2):
		GPIO.output(m2in3, 0)
		GPIO.output(m2in4, 0)

def motorReverse(num):
	if (num == 1):
		GPIO.output(m1in1, 0)
		GPIO.output(m1in2, 1)
	elif (num == 2):
		#GPIO.output(m2in3, 0)
		#GPIO.output(m2in4, 1)

try:
	while True:
		motorForward(1)
		motorForward(2)
		print("Currently going forward")
		time.sleep(1)
		motorOff(1)
		motorOff(2)
		print("Currently Off")
		time.sleep(1)
		motorReverse(1)
		motorReverse(2)
		print("Currently reversing")
		time.sleep(1)
		motorOff(1)
		motorOff(2)
		print("Currently Off")
		time.sleep(1)
except KeyboardInterrupt: 
	GPIO.cleanup();
		



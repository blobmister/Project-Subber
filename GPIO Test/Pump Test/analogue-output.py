import RPi.GPIO as GPIO
import time

m1in1 = 11
m1in2 = 13
m2in3 = 16
m2in4 = 15
m1pwmPin = 33
m2pwmPin = 32

GPIO.setmode(GPIO.BOARD)

GPIO.setup(m1in1, GPIO.OUT)
GPIO.setup(m1in2, GPIO.OUT)
GPIO.setup(m2in3, GPIO.OUT)
GPIO.setup(m2in4, GPIO.OUT)
GPIO.setup(m1pwmPin, GPIO.OUT)
GPIO.setup(m2pwmPin, GPIO.OUT)

m1pwm = GPIO.PWM(m1pwmPin, 10000)
m2pwm = GPIO.PWM(m2pwmPin, 10000)
m1pwm.start(0)
m2pwm.start(0)

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
		GPIO.output(m2in3, 0)
		GPIO.output(m2in4, 1)

motorForward(1)
motorForward(2)		

try:
	while True:
		for duty in range(0, 101, 1):
			m1pwm.ChangeDutyCycle(duty)
			m2pwm.ChangeDutyCycle(duty)
			time.sleep(0.2)
		
		print("Fully on")
		
		for duty in range(100, -1, -1):
			m1pwm.ChangeDutyCycle(duty)
			m2pwm.ChangeDutyCycle(duty)
			time.sleep(0.2)
		 
		print("Fully off")
		
except KeyboardInterrupt:
	m1pwm.stop()
	m2pwm.stop()
	GPIO.cleanup()		


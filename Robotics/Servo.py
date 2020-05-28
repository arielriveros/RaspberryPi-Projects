import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Servo_setup:
	# Constructor
	def __init__(self, pin):
		self.pin = pin
		GPIO.setup(pin,GPIO.OUT)
		self.servo = GPIO.PWM(pin,50)
		self.servo.start(0)
	"""
	method ChangeDutyCycle from GPIO.PWM
	gets as argument a float from 2.5 to 12.5 (ms)
	t:= duration
	"""
	def move(self,position,t):
		try:
			if(t!=0):
				while(position<=12.5):
					self.servo.ChangeDutyCycle(position)
					time.sleep(t)
					break
			elif(t==0):
				while(position<=12.5):
					self.servo.ChangeDutyCycle(position)
		except KeyboardInterrupt:
		    self.servo.stop()
		    self.clear()
	def clear(self):
		self.servo.stop()
		GPIO.cleanup(self.pin)


class Servo_control:
	def __init__(self,servo,initPos):
		self.servo=servo
		self.initPos=initPos
		self.servo.move(initPos,0.01)
	def minPos(self):
		self.servo.move(2.5,0.001)
	def moveTo45(self):
		self.servo.move(5,0.001)
	def moveTo90(self):
		self.servo.move(7.5,0.001)
	def moveTo135(self):
		self.servo.move(10,0.001)
	def maxPos(self):
		self.servo.move(12.5,0.001)
	def moveToInit(self):
		self.servo.move(self.initPos,0.01)
	def positiveSweep(self,time_step):
		self.minPos()
		time.sleep(0.1)
		for i in range(100):
			self.servo.move(2.5+(i/10),0.001)
			time.sleep(time_step)
		self.moveToInit()
	def negativeSweep(self,time_step):
		self.maxPos()
		time.sleep(0.1)
		for i in range(100):
			self.servo.move(12.5-(i/10),0.001)
			time.sleep(time_step)
		self.moveToInit()


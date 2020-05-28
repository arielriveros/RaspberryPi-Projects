import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class LED_setup:
	def __init__(self,pin):
		self.pin = pin
		GPIO.setup(self.pin,GPIO.OUT,initial=GPIO.LOW)
	def setOn(self):
		GPIO.output(self.pin,GPIO.HIGH)
	def setOff(self):
		GPIO.output(self.pin,GPIO.LOW)
	def reset(self):
		GPIO.cleanup(self.pin)
		
# this class controls leds as lists of elements type LED_setup
class LED_control:
	# Constructor
	def __init__(self):
		self.LEDs=[]
	# Add LED to the list
	def addLed(self,LED):
		self.LEDs.extend(LED)
	# turnAll('on') Turns all Leds On, 'off' -> Leds Off
	def turnAll(self,state):
		if state=='on':
			for i in self.LEDs:
				i.setOn()
		elif state=='off':
			for i in self.LEDs:
				i.setOff()
		else:
			print('unknown command')
	# turns On the Leds for t time from first to last
	def sequence(self, t,opt):
		self.turnAll('off')
		if opt=='exclusive':
			for i in self.LEDs:
				i.setOn()
				time.sleep(t)
				i.setOff()
		if opt=='inclusive':
			for i in self.LEDs:
				i.setOn()
				time.sleep(t)
		self.turnAll('off')
	# turns on and off all Leds in t periods of time
	def blink(self,t):
		self.turnAll('on')
		time.sleep(t/2)
		self.turnAll('off')
		time.sleep(t/2)
	def terminate(self):
		for i in self.LEDs:
			i.reset()





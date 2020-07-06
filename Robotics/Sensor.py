import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

class Sensor_setup:
	# Constructor
	def __init__(self,echo,trigger,green,yellow):
		self.echo = echo
		GPIO.setup(echo,GPIO.IN)

		self.trigger = trigger
		GPIO.setup(trigger,GPIO.OUT)

		self.green = green
		GPIO.setup(green,GPIO.OUT)

		self.yellow = yellow
		GPIO.setup(yellow,GPIO.OUT)

	def start(self,limit,show):
		GPIO.output(self.green,False)
		GPIO.output(self.yellow,False)
		try:
			while True:
				GPIO.output(self.trigger, True)
				time.sleep(0.2)

				GPIO.output(self.trigger, False)
				time.sleep(0.00001)
				GPIO.output(self.trigger,False)

				while GPIO.input(self.echo) == 0:
					pulse_start = time.time()

				while GPIO.input(self.echo) == 1:
					pulse_end = time.time()

				pulse_duration = pulse_end - pulse_start
				distance = pulse_duration*17150
				distance = round(distance,2)

				if(show == "True"):
					print (distance," cm")
					if(distance > limit):
						GPIO.output(self.green, True)
						GPIO.output(self.yellow, False)
					if(5.0 < distance <= limit):
						GPIO.output(self.green,False)
						GPIO.output(self.yellow,True)
					if(5.0 >= distance):
						GPIO.output(self.yellow,False)
						GPIO.output(self.green,False)
						time.sleep(0.1)
						GPIO.output(self.yellow,True)
				if(show == "False"):
                                        if(distance > limit):
                                                GPIO.output(self.green, True)
                                                GPIO.output(self.yellow, False)
                                        if(5.0 < distance <= limit):
                                                GPIO.output(self.green,False)
                                                GPIO.output(self.yellow,True)
                                        if(5.0 >= distance):
                                                GPIO.output(self.yellow,False)
                                                GPIO.output(self.green,False)
                                                time.sleep(0.1)
                                                GPIO.output(self.yellow,True)
		except KeyboardInterrupt:
			print("Stop")
			GPIO.cleanup()

import RPi.GPIO as GPIO
import time

pin = int(input("Pin: "))
time_active = int(input("Time: "))
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setup(pin, GPIO.OUT)

GPIO.output(pin,1)

time.sleep(time_active)
GPIO.output(pin,0)

GPIO.cleanup

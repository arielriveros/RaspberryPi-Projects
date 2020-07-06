import sys
sys.path.insert(1,'/home/pi/Documents/RaspberryPi-Projects/Robotics')
from Sensor import *

userInput = input("Show distance: ")

sensor = Sensor_setup(12,6,20,16)

sensor.start(10.0,userInput)

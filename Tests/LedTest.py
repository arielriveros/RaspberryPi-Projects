import importlib
import sys
sys.path.insert(1,'/home/pi/Documents/Programs/Robotics')
from time import sleep
from LEDs import LED_setup, LED_control

redLed=LED_setup(2)
blueLed=LED_setup(3)
greenLed=LED_setup(17)
yellowLed=LED_setup(18)
whiteLed=LED_setup(27)

control = LED_control()

control.addLed([redLed,blueLed,greenLed,yellowLed,
	whiteLed])
print("500ms Blink")
x=0
while(x<10):
	control.blink(0.5)
	x=x+1
print("100ms Inclusive Sequence")
x=0
while(x<10):
	control.sequence(0.1,'inclusive')
	x=x+1
print("100ms Exclusive Sequence")
x=0
while(x<10):
	control.sequence(0.1,'exclusive')
	x=x+1
x=0
print("10ms Exclusive Sequence")
while(x<100):
	control.sequence(0.01,'exclusive')
	x=x+1
x=0
print("100ms Blink")
while(x<50):
	control.blink(0.1)
	x=x+1
control.terminate()
print("Led Test Finished")

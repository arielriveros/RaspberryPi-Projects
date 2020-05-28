import sys
sys.path.insert(1,'/home/pi/Documents/Programs/Robotics')
from Servo import Servo_setup, Servo_control
import RPi.GPIO as GPIO
from time import sleep

servo_test = Servo_setup(21)

lis1=[2.5,3,4,5,6,7,8,9,10,11,12.5]
for i in lis1:
       	servo_test.move(i, .1)
for i in list(reversed(lis1)):
       	servo_test.move(i, .05)
lis2=[2.5,7.5,12.5]
for j in lis2:
	servo_test.move(j,.5)
for j in list(reversed(lis2)):
	servo_test.move(j,.5)

servo_test.clear()

servo_test2 = Servo_setup(21)
servo_control = Servo_control(servo_test2, 7.5)
sleep(1)
servo_control.moveTo45()
sleep(1)
servo_control.moveTo135()
sleep(1)
servo_control.moveTo90()
sleep(1)
servo_control.minPos()
sleep(1)
servo_control.maxPos()
sleep(1)
servo_control.moveToInit()
sleep(1)

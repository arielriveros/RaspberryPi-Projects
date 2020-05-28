import sys
sys.path.insert(1,'/home/pi/Documents/RaspberryPi-Projects/Robotics')
from Servo import Servo_setup, Servo_control
import RPi.GPIO as GPIO
from time import sleep

servo_test = Servo_setup(21)

lis1=[2.5,3,4,5,6,7,8,9,10,11,12.5]

print("Micro Servo SG90 Setup Test")

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
print("Servo Setup Test Finished")

servo_test2 = Servo_setup(21)
servo_control = Servo_control(servo_test2, 7.5)

print("Servo Control Test")
sleep(2)
print("Move to 45°")
servo_control.moveTo45()
sleep(1)
print("Move to 135°")
servo_control.moveTo135()
sleep(1)
print("Move to 90°")
servo_control.moveTo90()
sleep(1)
print("Move to 0°")
servo_control.minPos()
sleep(1)
print("Move to 180°")
servo_control.maxPos()
sleep(1)
print("...")
servo_control.moveToInit()
sleep(1)
print("Positive Sweep 10ms")
servo_control.positiveSweep(0.01)
sleep(2)
print("Positive Sweep 15ms")
servo_control.positiveSweep(0.015)
sleep(1)
print("Positive Sweep 30ms")
servo_control.positiveSweep(0.03)
print("...")
sleep(2)
print("Negative Sweep 10ms")
servo_control.negativeSweep(0.01)
sleep(1)
print("Negative Sweeo 15ms")
servo_control.negativeSweep(0.015)
sleep(1)
print("Negative Sweep 30ms")
servo_control.negativeSweep(0.03)
sleep(1)
print("Test Finished")

from gpiozero import Servo
from time import sleep

Pin = 21    # Posicion GPIO
Crt = 0.5   # Correcion

maxPW = ( 2.0 + Crt ) / 1000
minPW = ( 1.0 - Crt ) / 1000

servo = Servo( Pin
, min_pulse_width = minPW
, max_pulse_width = maxPW)

while True:
    servo.value = 0
    print("Centro")
    sleep(1)
    servo.value = None
    sleep(1)
    servo.value = -1
    print("Cerrado")
    sleep(1)
    servo.value = None
    sleep(1)
    servo.value = 0
    print("Centro")
    sleep(1)
    servo.value = None
    sleep(1)
    servo.value = 1
    print("Abierto")
    sleep(1)
    servo.value = None
    sleep(1)

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
    servo.mid()
    print("Centro")
    sleep(2)
    servo.min()
    print("Cerrado")
    sleep(2)
    servo.mid()
    print("Centro")
    sleep(2)
    servo.max()
    print("Abierto")
    sleep(2)

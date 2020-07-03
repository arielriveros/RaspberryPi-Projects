from LEDs import *

frontal = LED_setup(27)
rear1 = LED_setup(17)
rear2 = LED_setup(18)
leds = LED_control()
leds.addLed([frontal,rear1,rear2])

def main():
	while True:
		user_input = input("Fon Foff Ron Stop exit\n")
		if user_input == "Fon":
			frontal.setOn()
		elif user_input == "Foff":
			frontal.setOff()
		elif user_input == "Ron":
			rear1.setOn()
		elif user_input == "Stop":
			rear1.setOn()
			rear2.setOn()
			input()
			rear1.setOff()
			rear2.setOff()
		elif user_input == "exit":
			break
		else:
			print("error")

main()

leds.terminate()

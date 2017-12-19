import radio
import random
from microbit import display, Image, button_a, sleep

steps = list(range(5, 10)) + list(range(9, -1, -1))
animation = [Image().invert() * (i/9) for i in steps]

radio.on()
while True:
	if button_a.was_pressed():
		radio.send("flash")

	message = radio.receive()
	if message == "flash":
		sleep(random.randint(50, 350))
		display.show(animation, delay=60, wait=False)

		if random.random() < 0.1:
			sleep(500)
			radio.send("flash")  # re-broadcast

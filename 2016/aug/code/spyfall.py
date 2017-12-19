import radio
import random

from microbit import Image, display, button_a, button_b, sleep
from microbit import accelerometer, running_time


LOCATIONS = ["airplane", "bank", "beach", "cathedral", "casino",
    "circus", "corpo party", "crusade", "spa", "embassy", "hospital",
    "hotel", "military base", "movie studio", "ocean liner", "train",
    "pirate ship", "polar station", "police station", "restaurant",
    "school", "car service", "space station", "submarine", "supermarket",
    "theatre", "university"]


def play(location):
    display.show(Image.ALL_CLOCKS, delay=50, loop=True, wait=False)

    number = random.randrange(1, 10000)
    sleep(random.randrange(10, 500))
    radio.send(str(number))

    sleep(3000)

    numbers = []
    while True:
        message = radio.receive()
        if not message:
            break
        numbers.append(int(message))

    if number < min(numbers):
        location = "UNKNOWN"

    radio.off()

    display.show(Image.ARROW_E)

    seconds = 0
    start_time = running_time()
    button_b.was_pressed()

    while seconds < 8 * 60:
        if accelerometer.was_gesture("shake"):
            minutes = seconds // 60
            display.scroll("{0}:{1:02d}".format(minutes, seconds - minutes * 60))
        if button_b.was_pressed():
            display.scroll(location.upper())

        sleep(10)
        seconds = (running_time() - start_time) // 1000

    animation = [Image.SKULL, Image()]
    display.show(animation, delay=500, loop=True, wait=False)

    while True:
        sleep(10000)
        display.off()


def listen():
    location = radio.receive()
    if location:
        play(location)


def start():
    for i in range(5):
        sleep(500)
        if not (button_a.is_pressed() and button_b.is_pressed()):
            return

    location = random.choice(LOCATIONS)
    radio.send(location)
    play(location)


radio.on()
radio.config(length=16, queue=10, group=199, data_rate=radio.RATE_250KBIT)

display.show(Image.FABULOUS)

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        start()
    else:
        listen()

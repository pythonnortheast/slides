import radio

from microbit import Image, display, sleep
from microbit import button_a, button_b, accelerometer


ICONS = {
    "rock": Image("07970:79997:99999:79997:07970"),
    "paper": Image.SQUARE,
    "scissors": Image("90009:09090:00900:99099:99099"),
    "lizard": Image("99000:99770:00788:00088:06780"),
    "Spock": Image("90009:97079:99099:09790:00900")
}

WINNERS = {
    ("rock", "lizard"), ("rock", "scissors"),
    ("paper", "rock"), ("paper", "Spock"),
    ("scissors", "paper"), ("scissors", "lizard"),
    ("lizard", "paper"), ("lizard", "Spock"),
    ("Spock", "rock"), ("Spock", "scissors")
}


def compare(name):
    display.show(Image.ALL_CLOCKS, delay=100, loop=True, wait=False)
    radio.send(name)

    # wait for the message
    for i in range(1000):
        sleep(500)
        other = radio.receive()
        if other:
            break

    animation = [ICONS[name], Image(), ICONS[name]]
    display.show(animation, delay=200, loop=True, wait=False)
    sleep(5000)

    if name == other:
        display.show(Image.MEH)
    elif (name, other) in WINNERS:
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)
    sleep(5000)


radio.on()
radio.config(group=251)

i = 0
names = ["rock", "paper", "scissors", "lizard", "Spock"]

while True:
    name = names[i]
    display.show(ICONS[name])

    if accelerometer.was_gesture("shake"):
        compare(name)

    elif button_b.was_pressed():
        i = (i + 1) % 5

    elif button_a.was_pressed():
        i = (i - 1) % 5

    sleep(10)

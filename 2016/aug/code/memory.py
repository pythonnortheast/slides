import radio
import random

from microbit import Image, display, sleep, running_time
from microbit import button_a, button_b, accelerometer


ICONS = {
    "up": Image.ARROW_N,
    "down": Image.ARROW_S,
    "left": Image.ARROW_W,
    "right": Image.ARROW_E,
    "gg": Image.HAPPY,
    "timeout": Image("09990:90909:90999:90009:09990")
}

radio.on()
radio.config(group=163)

sequence = []


def wait_animation():
    images = [Image("0:0:00{0}00:0:0".format(i)) for i in range(2, 10)]
    images.extend(reversed(images))
    display.show(images, delay=75, loop=True, wait=False)


def sync():
    number = random.randrange(1, 10000)
    message = None

    while not message:
        radio.send(str(number))
        sleep(250)
        message = radio.receive()

    return number < int(message)


def read_move():
    x, y, z = accelerometer.get_values()
    if x > 500:
        return "right"
    if x < -500:
        return "left"
    if y > 800:
        return "down"
    if y < -300:
        return "up"
    return None


def add_new_move():
    display.show("?")

    move = read_move()
    while not move:
        move = read_move()

    display.show(ICONS[move])
    radio.send(move)
    sequence.append(move)
    sleep(2000)


def shutdown():
    while True:
        sleep(10000)
        display.off()


def receive_new_move():
    wait_animation()

    move = radio.receive()
    while move not in ICONS:
        sleep(100)
        move = radio.receive()

    display.show(ICONS[move])
    sequence.append(move)

    # other player lost the game
    if move == "gg":
        radio.off()
        shutdown()


def wait_for_button():
    while not (button_a.was_pressed() or button_b.was_pressed()):
        sleep(100)


def game_over(move):
    radio.send("gg")
    radio.off()

    images = [ICONS[move], Image(" ")]
    display.show(images, loop=True, wait=False)
    sleep(3000)

    display.show(Image.SAD)
    shutdown()


def read_sequence():
    display.show(Image("0:0:35753:0:0"))
    start = running_time()

    for i in range(len(sequence)):
        move = read_move()
        while not move:
            move = read_move()
            # check time
            if running_time() - start > (i + 1) * 5000:
                game_over("timeout")

        # is the move correct?
        if move == sequence[i]:
            display.show(ICONS[move])
            sleep(500)
            display.show(Image("0:0:34543:0:0"))
            sleep(300)
        else:
            game_over(sequence[i])


wait_animation()
is_first = sync()

if is_first:
    add_new_move()

while True:
    receive_new_move()
    wait_for_button()
    read_sequence()
    add_new_move()

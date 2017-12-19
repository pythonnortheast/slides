import radio
import random

from microbit import Image, display, sleep
from microbit import button_a, button_b

radio.on()
radio.config(group=101)


def blink(sprite, board):
    images = []
    for value in range(1, 10):
        image = board.copy()
        for x, y in sprite:
            image.set_pixel(x, y, value)
        images.append(image)

    images.extend(reversed(images))
    display.show(images, delay=75, loop=True, wait=False)


def move(sprite, dx, dy):
    sprite = [(x + dx, y + dy) for x, y in sprite]

    # check if sprite moved out of bounds
    x_shift = y_shift = 0
    if dx and any(x > 4 for x, y in sprite):
        x_shift = min(x for x, y in sprite)
    if dy and any(y > 4 for x, y in sprite):
        y_shift = min(y for x, y in sprite)

    # shift sprite to the first row/column
    if dx or dy:
        sprite = [(x - x_shift, y - y_shift) for x, y in sprite]
    return sprite


def position(sprite, board, send=False):
    blink(sprite, board)

    while not (button_a.is_pressed() and button_b.is_pressed()):
        sleep(100)
        # if button is pressed but not released yet, keep waiting
        if button_a.is_pressed() or button_b.is_pressed():
            continue

        a = button_a.was_pressed()
        b = button_b.was_pressed()
        if a or b:
            sprite = move(sprite, b, a)
            blink(sprite, board)
            if send:
                radio.send("{}{}".format(*sprite[0]))

    return sprite


def add_ship(sprite, board):
    while True:
        sprite = position(sprite, board)
        if sum(board.get_pixel(x, y) for x, y in sprite) == 0:
            break

    for x, y in sprite:
        board.set_pixel(x, y, 8)

    display.show(board)
    sleep(500)
    # wait for release of the buttons (to avoid accidental placement)
    while button_a.is_pressed() and button_b.is_pressed():
        sleep(100)


def horizontal(size):
    return [(x, 0) for x in range(size)]


def vertical(size):
    return [(0, y) for y in range(size)]


def setup():
    board = Image(" ")
    add_ship(vertical(3), board)
    add_ship(horizontal(3), board)
    add_ship(vertical(2), board)
    add_ship(horizontal(2), board)
    return board


def sync():
    display.show(Image.ALL_CLOCKS, delay=100, loop=True, wait=False)

    n = random.randrange(1, 10000)
    radio.send(str(n))

    message = None
    while not message:
        sleep(500)
        message = radio.receive()
    return n < int(message)


def game_over(image):
    display.show(image)
    radio.off()
    while True:
        sleep(10000)
        display.off()


def attack(board):
    target = [(1, 1)]
    while True:
        target = position(target, board, send=True)
        if board.get_pixel(*target[0]) == 0:
            break

    radio.send("fire")
    sleep(500)

    message = radio.receive()
    if message == "gg":
        game_over(Image.HAPPY)

    value = 8 if message == "hit" else 2
    board.set_pixel(target[0][0], target[0][1], value)

    display.show(board)
    sleep(2000)


def defend(board):
    message = None
    while message != "fire":
        if message:
            x, y = (int(i) for i in message)
            blink([(x, y)], board)
        sleep(100)
        message = radio.receive()

    hit = board.get_pixel(x, y) == 8
    board.set_pixel(x, y, 2)
    display.show(board)

    if hit:
        if "8" in repr(board):
            radio.send("hit")
        else:
            radio.send("gg")
            game_over(Image.SAD)
    else:
        radio.send("miss")

    sleep(2000)


my_board = setup()
other_board = Image(" ")

is_first = sync()
if is_first:
    attack(other_board)

while True:
    defend(my_board)
    attack(other_board)

import random

from collections import namedtuple

Move = namedtuple("Move", "board square")


def read_move():
	return Move(*map(int, input().split()))


def write_move(move):
	print(move.board, move.square)


while True:
	enemy_move = read_move()

	count = int(input())
	moves = [read_move() for i in range(count)]

	write_move(random.choice(moves))

from collections import namedtuple

Move = namedtuple("Move", "board square")

CORNERS = {0, 2, 6, 8}
CENTRE = 4


def read_move():
	return Move(*map(int, input().split()))


def write_move(move):
	print(move.board, move.square)


def evaluate(move):
	if move.square in CORNERS:
		return 2
	if move.square == CENTRE:
		return 1
	return 0


while True:
	enemy_move = read_move()

	count = int(input())
	moves = [read_move() for i in range(count)]

	move = max(moves, key=evaluate)
	write_move(move)

from collections import namedtuple

Move = namedtuple("Move", "board square")

DIAGONALS = ((0, 4, 8), (2, 4, 6))
COLUMNS = ((0, 3, 6), (1, 4, 7), (2, 5, 8))
ROWS = ((0, 1, 2), (3, 4, 5), (6, 7, 8))
LINES = ROWS + COLUMNS + DIAGONALS

CORNERS = {0, 2, 6, 8}
CENTRE = 4


def read_move():
	return Move(*map(int, input().split()))


def write_move(move):
	print(move.board, move.square)


def evaluate(move):
	current = boards[move.board].copy()
	current[move.square] = 1

	if any(sum(current[x] for x in line) == 3 for line in LINES):
		return 10
	if move.square in CORNERS:
		return 2
	if move.square == CENTRE:
		return 1
	return 0


boards = tuple([0 for i in range(9)] for i in range(9))

while True:
	# place opponents move
	enemy_move = read_move()
	if enemy_move.board >= 0:
		boards[enemy_move.board][enemy_move.square] = -1

	count = int(input())
	moves = [read_move() for i in range(count)]

	move = max(moves, key=evaluate)
	write_move(move)

	# place my move
	boards[move.board][move.square] = 1

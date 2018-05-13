from copy import deepcopy
from collections import namedtuple

Move = namedtuple("Move", "board square")
State = namedtuple("State", "meta boards")

DIAGONALS = ((0, 4, 8), (2, 4, 6))
COLUMNS = ((0, 3, 6), (1, 4, 7), (2, 5, 8))
ROWS = ((0, 1, 2), (3, 4, 5), (6, 7, 8))
LINES = ROWS + COLUMNS + DIAGONALS


def read_move():
	return Move(*map(int, input().split()))


def write_move(move):
	print(move.board, move.square)


def has_line(board, player=1):
	return any(sum(board[x] for x in line) == player * 3 for line in LINES)


def under_threat(board):
	return any(sum(board[x] for x in line) == -2 for line in LINES)


def update(state, move, player=1):
	current = state.boards[move.board]
	current[move.square] = player

	if has_line(current, player):
		state.meta[move.board] = player

	return current


def evaluate(move):
	new_state = deepcopy(state)
	new_board = update(new_state, move)
	next_board = new_state.boards[move.square]

	if has_line(new_state.meta):
		return 100

	new_state.meta[move.square] = -1
	if has_line(new_state.meta, -1) and under_threat(next_board):
		return -100

	if has_line(new_board):
		return 10

	# TODO: what if the next board is out of play (full or has a line)?
	#       need to check all other boards for threats

	if under_threat(next_board):
		return -10

	# TODO: should we give extra points to moves that put the current
	#       board under our threat?

	return 0


meta = [0 for i in range(9)]
board = tuple([0 for i in range(9)] for i in range(9))
state = State(meta, board)

while True:
	# place opponents move
	enemy_move = read_move()
	if enemy_move.board >= 0:
		update(state, enemy_move, -1)

	count = int(input())
	moves = [read_move() for i in range(count)]

	move = max(moves, key=evaluate)
	write_move(move)

	# place my move
	update(state, move)

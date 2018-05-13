import sys
import time
import random
import statistics
import itertools

from copy import deepcopy
from collections import namedtuple

Move = namedtuple("Move", "board square")
State = namedtuple("State", "meta boards")

DIAGONALS = ((0, 4, 8), (2, 4, 6))
COLUMNS = ((0, 3, 6), (1, 4, 7), (2, 5, 8))
ROWS = ((0, 1, 2), (3, 4, 5), (6, 7, 8))
LINES = ROWS + COLUMNS + DIAGONALS
DEPTH = 4


def read_move():
	return Move(*map(int, input().split()))


def write_move(move):
	print(move.board, move.square)


def has_line(board, player=1):
	return any(sum(board[x] for x in line) == player * 3 for line in LINES)


def under_threat(board, player=1):
	return any(sum(board[x] for x in line) == player * 2 for line in LINES)


def game_over(meta):
	return any(abs(sum(meta[x] for x in line)) == 3 for line in LINES)


def valid_moves(state, next_board):
	# next board is playable (not captured and not full)
	if (state.meta[next_board] == 0 and not all(state.boards[next_board])):
		return (Move(next_board, x) for x in range(9) if state.boards[next_board][x] == 0)

	# cannot play on the next board, list valid moves on all other boards
	boards = (x for x in range(9) if state.meta[x] == 0)
	return (Move(b, x) for b in boards for x in range(9) if state.boards[b][x] == 0)


def update(state, move, player=1):
	current = state.boards[move.board]
	current[move.square] = player

	if has_line(current, player):
		state.meta[move.board] = player

	return current


def evaluate(state, move, player=1):
	new_state = deepcopy(state)
	new_board = update(new_state, move, player)
	next_board = new_state.boards[move.square]

	if has_line(new_state.meta, player):
		return 100

	new_state.meta[move.square] = -player
	if has_line(new_state.meta, -player) and under_threat(next_board, -player):
		return -100

	# TODO: is this working well when multiple move has been made?

	# TODO: does it matter that we can complete one grid if the opponent
	#       can complete two in the same playout?

	# TODO: do all grids count the same? should we value centre and corners more?

	if has_line(new_board, player):
		return 10

	if under_threat(next_board, -player):
		return -10

	if under_threat(new_state.meta, player):
		return 5

	# free grid choice for the opponent
	if new_state.meta[move.square] != 0:
		return -5

	return 0


def random_play(move):
	new_state = deepcopy(state)
	player = 1

	for i in range(0, DEPTH):
		update(new_state, move, player)
		if game_over(new_state.meta):
			return player * 100

		next_moves = list(valid_moves(new_state, move.square))
		if not next_moves:
			return sum(new_state.meta) * 20  # difference in captured boards

		move = random.choice(next_moves)
		player = -1 * player

	return evaluate(new_state, move)


def best_play(moves, start_time):
	runs = 0
	scores = [0] * len(moves)

	for i, move in itertools.cycle(enumerate(moves)):
		# stop when running out of time
		if (time.perf_counter() - start_time) > 0.097:
			break
		# best score at the end of a random play is the move score
		scores[i] = max(scores[i], random_play(move))
		runs += 1

	print("runs =", runs, file=sys.stderr)
	print(scores, file=sys.stderr)
	best_index = max(range(len(moves)), key=lambda x: scores[x])
	return moves[best_index]


def report_time(times, start_time):
	new_time = time.perf_counter()
	times.append(new_time - start_time)
	print((3 * "{:.6f} ").format(min(times), statistics.median(times), max(times)), file=sys.stderr)


meta = [0 for i in range(9)]
board = tuple([0 for i in range(9)] for i in range(9))
state = State(meta, board)

times = []

while True:
	enemy_move = read_move()
	count = int(input())
	moves = [read_move() for i in range(count)]

	start_time = time.perf_counter()

	# play first move in the centre
	if enemy_move.board < 0:
		move = Move(4, 4)

	# place enemy move and choose the best response
	else:
		update(state, enemy_move, -1)
		move = best_play(moves, start_time)

	write_move(move)
	report_time(times, start_time)

	# place my move
	update(state, move)

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


def under_threat(board, player=1):
	return any(sum(board[x] for x in line) == player * 2 for line in LINES)


def game_over(meta):
	return any(abs(sum(meta[x] for x in line)) == 3 for line in LINES)


def valid_moves(state, next_board):
	if game_over(state.meta):
		return []

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


def evaluate(state, move, player):
	new_state = deepcopy(state)
	new_board = update(new_state, move, player)
	next_board = new_state.boards[move.square]

	if has_line(new_state.meta, player):
		return 100

	new_state.meta[move.square] = -player
	if has_line(new_state.meta, -player) and under_threat(next_board, -player):
		return -100

	if has_line(new_board, player):
		return 10

	if under_threat(next_board, -player):
		return -10

	if under_threat(new_state.meta, player):
		return 5

	# free grid choice for the opponent
	if new_state.meta[move.square] != 0:
		return -5

	# TODO: should we add up all the positives and negatives together?

	# TODO: what if the opponent plays defensively? how to value the moves then?

	return 0


def best_enemy_play(move):
	new_state = deepcopy(state)
	update(new_state, move)

	best = -1000
	for enemy_move in valid_moves(new_state, move.square):
		best = max(best, evaluate(new_state, enemy_move, -1))
	return best


meta = [0 for i in range(9)]
board = tuple([0 for i in range(9)] for i in range(9))
state = State(meta, board)

while True:
	enemy_move = read_move()
	count = int(input())
	moves = [read_move() for i in range(count)]

	# play first move in the centre
	if enemy_move.board < 0:
		move = Move(4, 4)

	# place enemy move and choose response
	else:
		update(state, enemy_move, -1)
		move = min(moves, key=best_enemy_play)

	write_move(move)

	# place my move
	update(state, move)

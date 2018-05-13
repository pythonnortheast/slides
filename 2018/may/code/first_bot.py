while True:
	board, square = [int(x) for x in input().split()]

	count = int(input())

	moves = []
	for i in range(count):
		board, square = [int(x) for x in input().split()]
		moves.append((board, square))

	move = moves[0]
	print(move[0], move[1])

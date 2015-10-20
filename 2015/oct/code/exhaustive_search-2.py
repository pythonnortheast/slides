#!/usr/bin/env python
"""
Exhaustive search. Prints best solution found so far.
Checks all (26 + 1)**14 possible strings.

"""
import string
import itertools

TARGET = "CHARLES DARWIN"
CHARACTERS = string.ascii_uppercase + " "


def evaluate(solution):
	return sum(1 for s,t in zip(solution, TARGET) if s != t)


best = len(TARGET)

for candidate in itertools.product(CHARACTERS, repeat=len(TARGET)):
	distance = evaluate(candidate)
	if distance < best:
		best = distance
		print("{0:02} {1}".format(distance, "".join(candidate)))

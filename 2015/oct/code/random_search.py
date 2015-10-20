#!/usr/bin/env python
"""
Random search. Generates an independent random solution at each step.
Does not care about repetitions. Prints best solution found so far.

"""
import string
import random

TARGET = "CHARLES DARWIN"
CHARACTERS = string.ascii_uppercase + " "


def evaluate(solution):
	return sum(1 for s,t in zip(solution, TARGET) if s != t)


best = len(TARGET)

while(True):
	candidate = [random.choice(CHARACTERS) for i in range(len(TARGET))]
	distance = evaluate(candidate)

	if distance < best:
		best = distance
		print("{0:02} {1}".format(distance, "".join(candidate)))

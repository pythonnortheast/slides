#!/usr/bin/env python
"""
Hill climbing. Randomises the best solution so far to generate the current one.
The mutation rate is controlled with the MUTATION_CHANCE parameter.
Prints current solution. Should be run in a terminal for the best effect.

QUESTION: does low or high mutation chance work better?

"""
from __future__ import print_function

import sys
import time
import string
import random

TARGET = "CHARLES DARWIN"
CHARACTERS = string.ascii_uppercase + " "

MUTATION_CHANCE = 0.1


def evaluate(solution):
	return sum(1 for s,t in zip(solution, TARGET) if s != t)


def mutate(solution):
	f = lambda x: random.choice(CHARACTERS) if random.random() < MUTATION_CHANCE else x
	return [f(x) for x in solution]


best = [random.choice(CHARACTERS) for i in range(len(TARGET))]
fitness = evaluate(best)

for i in range(1000000):
	candidate = mutate(best)
	distance = evaluate(candidate)

	print("[{0: 4}] {1:02} {2}".format(i, distance, "".join(candidate)), end="\r")
	sys.stdout.flush()

	# TODO: uncomment to slow down the process to watchable speed
	#time.sleep(0.01)

	if distance < fitness:
		fitness = distance
		best = candidate

	if fitness == 0:
		print()
		break

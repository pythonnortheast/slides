#!/usr/bin/env python
"""
Hill climbing. Randomises the best solution so far to generate the current one.
Prints current solution. Should be run in a terminal for the best effect.

QUESTION: is the current solution always improving?

"""
from __future__ import print_function

import sys
import time
import string
import random

TARGET = "CHARLES DARWIN"
CHARACTERS = string.ascii_uppercase + " "


def evaluate(solution):
	return sum(1 for s,t in zip(solution, TARGET) if s != t)


best = [random.choice(CHARACTERS) for i in range(len(TARGET))]
fitness = evaluate(best)

for i in range(1000000):
	candidate = best[:]

	k = random.randrange(0, len(TARGET))
	candidate[k] = random.choice(CHARACTERS)

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

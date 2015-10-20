import string
import random

possibleCharacters = string.ascii_uppercase + " "

target = "CHARLES DARWIN"

best_candidate = random.sample(possibleCharacters, len(target))
best_fitness = sum(1 for b,t in zip(best_candidate, target) if b != t)

for i in xrange(1000000000000):
	letter = random.choice(possibleCharacters)
	k = random.randint(0, len(target) - 1)

	best_candidate[k] = letter
	fitness = sum(1 for b,t in zip(best_candidate, target) if b != t)
	if fitness < best_fitness:
		best_fitness = fitness
		print("".join(best_candidate), i)

	if best_fitness == 0:
		print("done", i)
		break

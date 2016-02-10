#!/usr/bin/env python
"""
Tournament selection. Individuals used to generate the new population are
selected according to their fitness. Out of a tournament with TOURNAMENT_SIZE
participants, only the winner is selected (survival of the fittest).
Prints best, worst and median fitness of individuals in the final population.

QUESTION: does it work? what is wrong?

"""
import string
import random

TARGET = "CHARLES DARWIN"
CHARACTERS = string.ascii_uppercase + " "

GENERATIONS = 50
POPULATION_SIZE = 100
TOURNAMENT_SIZE = 3
MUTATION_PROBABILITY = 0.9
MUTATION_CHANCE = 0.1


def evaluate(solution):
	return sum(1 for s,t in zip(solution, TARGET) if s != t)


def init():
	return [random.choice(CHARACTERS) for i in range(len(TARGET))]


def mutate(solution):
	f = lambda x: random.choice(CHARACTERS) if random.random() < MUTATION_CHANCE else x
	return [f(x) for x in solution]


def select(population, k, tournament_size):
	chosen = []
	for i in range(k):
		candidates = random.sample(population, tournament_size)
		chosen.append(min(candidates))
	return chosen

def variate(population):
	for i in range(len(population)):
		if random.random() < MUTATION_PROBABILITY:
			population[i] = mutate(population[i])
	return population


population = [init() for i in range(POPULATION_SIZE)]
fitnesses = [evaluate(individual) for individual in population]

for i in range(GENERATIONS):
	# TODO: uncomment to watch changes between populations
	#for p in population:
		#print("".join(p) + "|"),
	#print()

	chosen = select(population, len(population), TOURNAMENT_SIZE)
	population = variate(chosen)
	fitnesses = [evaluate(individual) for individual in population]

fitnesses.sort()
params = fitnesses[0], fitnesses[-1], fitnesses[POPULATION_SIZE / 2]
print("best={0}, worst={1}, median={2}".format(*params))

#!/usr/bin/env python
"""
Population of random solutions. Mutates current population to generate the next.
The MUTATION_PROBABILITY parameter controls the proportion of individuals in the
population that are mutated (the rest is copied without changes).
Prints best, worst and median fitness of individuals in the final population.

QUESTION: does it work? what is missing?

"""
import string
import random

TARGET = "CHARLES DARWIN"
CHARACTERS = string.ascii_uppercase + " "

GENERATIONS = 50
POPULATION_SIZE = 100
MUTATION_PROBABILITY = 0.9
MUTATION_CHANCE = 0.1


def evaluate(solution):
	return sum(1 for s,t in zip(solution, TARGET) if s != t)


def init():
	return [random.choice(CHARACTERS) for i in range(len(TARGET))]


def mutate(solution):
	f = lambda x: random.choice(CHARACTERS) if random.random() < MUTATION_CHANCE else x
	return [f(x) for x in solution]


def variate(population):
	for i in range(len(population)):
		if random.random() < MUTATION_PROBABILITY:
			population[i] = mutate(population[i])
	return population


population = [init() for i in range(POPULATION_SIZE)]
fitnesses = [evaluate(individual) for individual in population]

for i in range(GENERATIONS):
	population = variate(population)
	fitnesses = [evaluate(individual) for individual in population]

fitnesses.sort()
params = fitnesses[0], fitnesses[-1], fitnesses[POPULATION_SIZE / 2]
print("best={0}, worst={1}, median={2}".format(*params))

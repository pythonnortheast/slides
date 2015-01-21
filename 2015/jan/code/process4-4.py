#!/usr/bin/evn python
# coding=utf-8
"""
Emergent art. Process 4.

"""
import math
import random
import itertools
import pyprocessing as p

SIZE = 400  # screen size
SCALE = 5  # number of elements
ROTATION = 0.02  # element rotation step


class Element:
	def __init__(self):
		self.x = random.randrange(int(0.25 * SIZE), int(0.75 * SIZE))
		self.y = random.randrange(int(0.25 * SIZE), int(0.75 * SIZE))
		self.size = random.randrange(5, int(0.2 * SIZE))

		# screen constraints
		self.min = self.size / 2
		self.max = SIZE - self.size / 2 - 1

		# random angle in radians
		self.angle = random.random() * 2 * math.pi
		# rotate a unit vector by angle
		self.velocity = [math.cos(self.angle), math.sin(self.angle)]

	def move(self):
		self.x += self.velocity[0]
		self.y += self.velocity[1]

		if not self.min < self.x < self.max:
			self.x -= self.velocity[0]
		if not self.min < self.y < self.max:
			self.y -= self.velocity[1]

	def rotate(self):
		self.angle += ROTATION
		self.velocity = [math.cos(self.angle), math.sin(self.angle)]


elements = [Element() for i in range(SCALE)]

def setup():
	p.size(SIZE, SIZE)
	p.noFill()
	p.stroke(255)

def draw():
	p.background(0)
	for e in elements:
		p.ellipse(e.x, e.y, e.size, e.size)
		p.line(e.x, e.y, e.x + e.velocity[0] * e.size / 2,
			e.y + e.velocity[1] * e.size / 2)

	# find all elements touching another element
	touching = {}
	for a, b in itertools.combinations(elements, 2):
		distance = math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)
		if distance < 0.5 * (a.size + b.size):
			touching[a] = True
			touching[b] = True

	# rotate and move all elements
	for e in elements:
		if e in touching:
			e.rotate()
		e.move()

p.run()

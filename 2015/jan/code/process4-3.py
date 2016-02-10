#!/usr/bin/evn python
# coding=utf-8
"""
Emergent art. Process 4.

"""
import math
import random
import pyprocessing as p

SIZE = 400 # screen size
SCALE = 3  # number of elements


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


elements = [Element() for i in range(SCALE)]

def setup():
	p.size(SIZE, SIZE)
	p.noFill()
	p.stroke(255)

def draw():
	p.background(0)
	for e in elements:
		p.ellipse(e.x, e.y, e.size, e.size)
		e.move()

p.run()

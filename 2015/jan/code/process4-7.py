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
SCALE = 200  # number of elements
ROTATION = 0.02  # element rotation step


class Element:
	def __init__(self):
		# TODO: what happens if you change the size of the elements?
		self.x = random.randrange(int(0.25 * SIZE), int(0.75 * SIZE))
		self.y = random.randrange(int(0.25 * SIZE), int(0.75 * SIZE))
		self.size = random.randrange(5, int(0.2 * SIZE))

		# list of touching elements
		self.touching = []

		# screen constraints
		self.min = self.size / 2
		self.max = SIZE - self.size / 2 - 1

		# random angle in radians
		self.angle = random.random() * 2 * math.pi
		# rotate a unit vector by angle
		self.velocity = [math.cos(self.angle), math.sin(self.angle)]

	def update(self, velocity):
		self.x += velocity[0]
		self.y += velocity[1]

		if not self.min < self.x < self.max:
			self.x -= velocity[0]
		if not self.min < self.y < self.max:
			self.y -= velocity[1]

	def move(self):
		self.update(self.velocity)

	def move_away(self):
		net_velocity = self.velocity[:]
		for element in self.touching:
			size = 3 * (self.size + element.size)
			net_velocity[0] += (self.x - element.x) / size
			net_velocity[1] += (self.y - element.y) / size

		self.touching = []
		self.update(net_velocity)

	def rotate(self):
		self.angle += ROTATION
		self.velocity = [math.cos(self.angle), math.sin(self.angle)]


elements = [Element() for i in range(SCALE)]

def setup():
	p.size(SIZE, SIZE)
	p.background(0)

def draw():
	# find all elements touching another element
	lines = []
	for a, b in itertools.combinations(elements, 2):
		distance = math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)
		if distance < 0.5 * (a.size + b.size):
			a.touching.append(b)
			b.touching.append(a)
			lines.append((a.x, a.y, b.x, b.y, distance))

	if lines:
		# TODO: what happens when you reverse the sort order?
		# sort lines by length
		lines.sort(key=lambda x: x[-1])

		# map distance to colour
		scale = 255.0 / len(lines)
		colours = (scale * i for i in range(len(lines)))

		# draw lines between elements
		for colour, line in itertools.izip(colours, lines):
			p.stroke(colour, 10)
			p.line(line[0], line[1], line[2], line[3])

	# move all elements
	for e in elements:
		if e.touching:
			e.rotate()
			e.move_away()
		else:
			e.move()

def mousePressed():
	if p.frame.loop:
		p.noLoop()
	else:
		p.loop()

p.run()

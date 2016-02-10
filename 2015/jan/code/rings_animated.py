#!/usr/bin/evn python
# coding=utf-8
"""
Rings animated.

"""
import math
import random
import pyprocessing as p

COLOURS = [(45,25,100), (345,50,65), (10,60,90), (30,50,100)]

class Ring:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.n = random.randint(3, 30)
		self.radius = random.randint(10, 100)
		self.size = random.randint(3, 15)
		self.colour = random.choice(COLOURS)

		self.angle = random.random() * 2*math.pi
		self.speed = p.map(self.radius, 10, 100, 0.03, 0.01)

		# randomise direction of rotation
		if random.random() > 0.5:
			self.speed *= -1

	def draw(self):
		p.fill(*self.colour)
		for i in range(self.n):
			angle = i * 2*math.pi / self.n + self.angle
			new_x = self.x + math.cos(angle) * self.radius
			new_y = self.y + math.sin(angle) * self.radius
			p.ellipse(new_x, new_y, self.size, self.size)

		self.angle += self.speed


rings = []

def setup():
	p.size (600, 200)
	p.colorMode(p.HSB, 360, 100, 100)
	p.noStroke()
	add(random.randint(0, 600), random.randint(0, 200))

def draw():
	p.background(292, 40, 30)
	for ring in rings:
		ring.draw()

def add(x, y):
	for i in range(10):
		ring = Ring(x, y)
		rings.append(ring)

def mousePressed():
	if p.mouse.button == p.LEFT:
		add(p.mouse.x, p.mouse.y)
	else:
		for i in range(10):
			rings.pop()

p.run()

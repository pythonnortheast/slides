#!/usr/bin/evn python
# coding=utf-8
"""
Rings.

"""
import math
import random
import pyprocessing as p

COLOURS = [(45,25,100), (345,50,65), (10,60,90), (30,50,100)]

p.size (600, 200)
p.colorMode(p.HSB, 360, 100, 100)
p.noStroke()
p.background(292, 40, 30)

x = random.randint(200, 400)
y = random.randint(5, 150)
n = random.randint(3, 30)
radius = random.randint(10, 100)
size = random.randint(3, 15)
colour = random.choice(COLOURS)

p.fill(*colour)
for i in range(n):
	angle = i * 2*math.pi / n
	new_x = x + math.cos(angle) * radius
	new_y = y + math.sin(angle) * radius
	p.ellipse(new_x, new_y, size, size)

p.run()

#!/usr/bin/evn python
# coding=utf-8
"""
Dark light.

"""
import pyprocessing as p

MAX_DISTANCE = p.dist(0, 0, 640, 360)


def setup():
	p.size(640, 360)
	p.noStroke()

def draw():
	p.background(0)

	for i in range(width / 20 + 1):
		for j in range(height / 20 + 1):
			size = p.dist(p.mouse.x, p.mouse.y, i * 20, j * 20)
			size = size / MAX_DISTANCE * 66
			p.ellipse(i * 20, j * 20, size, size)

p.run()

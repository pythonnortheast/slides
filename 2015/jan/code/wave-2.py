#!/usr/bin/evn python
# coding=utf-8
"""
Wave.

"""
import math
import pyprocessing as p

SPEED = 0.02


def setup():
	p.size(400, 400)
	p.colorMode(p.HSB, 360, 100, 100)
	p.fill(30, 100, 100)
	p.noStroke()

def draw():
	p.background(0)

	for i in range(20):
		angle = i * 0.2 + p.frame.count * SPEED
		x = i * 20
		y = (math.sin(angle) + 1) * 200
		p.ellipse(x, y, 16, 16)

p.run()

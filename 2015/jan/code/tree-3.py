#!/usr/bin/evn python
# coding=utf-8
"""
Tree.

"""
import math
import pyprocessing as p

def setup():
	p.size(400, 400)
	p.stroke(255)

def draw():
	p.background(0)

	# draw tree trunk and move to its top
	p.translate(200, 400)
	p.line(0, 0, 0, -120)
	p.translate(0, -120)

	angle = math.pi * p.mouse.x / 800

	# draw the branches
	branches(120, angle)

def branches(height, angle):
	height *= 0.66

	# finish branching when height is small
	if height < 3:
		return

	# draw left and right branch
	for angle in [-angle, angle]:
		p.pushMatrix()
		p.rotate(angle)
		p.line(0, 0, 0, -height)
		p.translate(0, -height)
		branches(height, angle)
		p.popMatrix()

p.run()

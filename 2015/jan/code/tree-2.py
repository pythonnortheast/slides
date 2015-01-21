#!/usr/bin/evn python
# coding=utf-8
"""
Tree.

"""
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

	# draw the branches
	branches(120)

def branches(height):
	height *= 0.66

	# finish branching when height is small
	if height < 3:
		return

	# draw left and right branch
	for angle in [-0.5, 0.5]:
		p.pushMatrix()
		p.rotate(angle)
		p.line(0, 0, 0, -height)
		p.translate(0, -height)
		branches(height)
		p.popMatrix()

p.run()

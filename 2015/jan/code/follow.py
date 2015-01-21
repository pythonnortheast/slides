#!/usr/bin/evn python
# coding=utf-8
"""
Follow.

"""
import math
import pyprocessing as p

# TODO: try changing size or segment length
LENGTH = 20
SIZE = 2

x = [0] * SIZE
y = [0] * SIZE

def setup():
	p.size(400, 400)
	p.strokeWeight(10)
	p.stroke(255, 200)

def draw():
	p.background(0)
	# direct first segment towards the mouse pointer
	drag_segment(0, p.mouse.x, p.mouse.y)
	for i in range(SIZE - 1):
		drag_segment(i + 1, x[i], y[i])

def drag_segment(i, head_x, head_y):
	# find the inclination of a segment with respect to X axis
	angle = math.atan2(head_y - y[i], head_x - x[i])
	# find tail position by rotating a segment around its head point
	x[i] = head_x - math.cos(angle) * LENGTH
	y[i] = head_y - math.sin(angle) * LENGTH

	# draw a segment (tail to head)
	p.pushMatrix()
	p.translate(x[i], y[i])
	p.rotate(angle)
	p.line(0, 0, LENGTH, 0)
	p.popMatrix()

p.run()

#!/usr/bin/evn python
# coding=utf-8
"""
Composition. Square Limit.

"""
import math
import pyprocessing as p

p.size(800, 800)
p.background(255)
p.translate(300, 300)

img = p.loadImage("fish.png")

def fish():
	p.image(img, -80, -80)

def rotate(f):
	def wrapped_f():
		p.pushMatrix()
		p.translate(0, 240)
		p.rotate(-math.pi / 2)
		f()
		p.popMatrix()
	return wrapped_f

def flip(f):
	def wrapped_f():
		p.pushMatrix()
		p.translate(240, 0)
		p.applyMatrix(
			-1, 0, 0, 0,
			0, 1, 0, 0,
			0, 0, 1, 0,
			0, 0, 0, 1)
		f()
		p.popMatrix()
	return wrapped_f

fish()

composition = flip(fish)
composition()

p.run()

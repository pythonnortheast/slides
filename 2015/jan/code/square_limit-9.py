#!/usr/bin/evn python
# coding=utf-8
"""
Composition. Square Limit.

"""
import math
import pyprocessing as p

p.size(800, 800)
p.background(255)
p.scale(3.3)

img = p.loadImage("fish.png")

def fish():
	p.image(img, -80, -80)

def blank():
	pass

def transform(t, *args):
	def wrapper(*args):
		def wrapped_f():
			p.pushMatrix()
			t(*args)  # perform transformation t
			args[-1]()  # call last argument as function
			p.popMatrix()
		return wrapped_f
	return wrapper

def overlay(*args):
	def wrapped_f():
		for f in args:
			f()
	return wrapped_f

@transform
def rotate(f):
	p.translate(0, 240)
	p.rotate(-math.pi / 2)

@transform
def rot45(f):
	p.rotate(-math.pi / 4)
	p.scale(1 / math.sqrt(2))

@transform
def flip(f):
	p.translate(240, 0)
	p.scale(-1, 1)

@transform
def above(*args):
	scale = 1.0 / len(args)
	p.scale(1, scale)
	for f in args[:-1]:
		f()
		p.translate(0, 240)

@transform
def beside(*args):
	scale = 1.0 / len(args)
	p.scale(scale, 1)
	for f in args[:-1]:
		f()
		p.translate(240, 0)


fish2 = flip(rot45(fish))
fish3 = rotate(rotate(rotate(fish2)))

t = overlay(fish, fish2, fish3)
u = overlay(fish2, rotate(fish2), rotate(rotate(fish2)), rotate(rotate(rotate(fish2))))

def grid2x2(a, b, c, d):
	return above(beside(a, b), beside(c, d))

def side(n):
	if n < 2:
		return grid2x2(blank, blank, rotate(t), t)
	return grid2x2(side(n - 1), side(n - 1), rotate(t), t)

def corner(n):
	if n < 2:
		return grid2x2(blank, blank, blank, u)
	return grid2x2(corner(n - 1), side(n -1), rotate(side(n - 1)), u)

def grid3x3(a, b, c, d, e, f, g, h, i):
	return above(beside(a, b, c), beside(d, e, f), beside(g, h, i))

def square(n):
	return grid3x3(
		corner(n), side(n), rotate(rotate(rotate(corner(n)))),
		rotate(side(n)), u, rotate(rotate(rotate(side(n)))),
		rotate(corner(n)), rotate(rotate(side(n))), rotate(rotate(corner(n)))
	)

# TODO: try changing the level
composition = square(3)
composition()

p.run()

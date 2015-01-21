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

def transform(t, *args):
	def wrapper(*args):
		def wrapped_f():
			p.pushMatrix()
			t(*args)  # perform transformation t
			args[-1]()  # call function f
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


fish2 = flip(rot45(fish))
fish3 = rotate(rotate(rotate(fish2)))

t = overlay(fish, fish2, fish3)
u = overlay(fish2, rotate(fish2), rotate(rotate(fish2)), rotate(rotate(rotate(fish2))))

t()
#TODO: try u() instead

p.run()

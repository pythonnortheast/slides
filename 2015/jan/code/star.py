#!/usr/bin/evn python
# coding=utf-8
"""
Star.

"""
import math
import pyprocessing as p


p.size(400, 400)
p.colorMode(p.HSB, 360, 100, 100, 100)
p.noStroke()

p.background(0)
# TODO: try to change the alpha value
p.fill(0, 100, 100, 40)

# shift the (0, 0) point
p.translate(200, 200)

# TODO: try to change the number of triangles
for i in range(10):
	# rotate around (0, 0) by 1/10th of a full angle
	p.rotate(2 * math.pi / 10)
	p.triangle(0, -200, 100, 100, -100, 100)

p.run()

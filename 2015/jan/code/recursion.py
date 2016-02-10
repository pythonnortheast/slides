#!/usr/bin/evn python
# coding=utf-8
"""
Recursion.

"""
import pyprocessing as p

p.size(400, 400)
p.noStroke()

def circle(x, radius, level):
	p.fill(126 * level / 4)
	p.ellipse(x, 200, radius * 2, radius * 2)

	if level > 1:
		circle(x - 0.5 * radius, 0.5 * radius, level - 1)
		circle(x + 0.5 * radius, 0.5 * radius, level - 1)

# TODO: try more/less levels
circle(200, 200, 6)

p.run()

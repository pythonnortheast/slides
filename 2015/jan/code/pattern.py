#!/usr/bin/evn python
# coding=utf-8
"""
Pattern.

"""
import pyprocessing as p

p.size(255, 255)

for x in range(256):
	for y in range(256):
		colour = x ^ y
		p.stroke(colour)
		p.point(x, y)

p.run()


"""
^ is bitwise exclusive or (xor)

0 ^ 0 = 1 ^ 1 = 0
1 ^ 0 = 0 ^ 1 = 1

Example: 100101 ^ 101001 = 001100

"""

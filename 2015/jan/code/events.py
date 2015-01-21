#!/usr/bin/evn python
# coding=utf-8
"""
Event handlers.

"""
import pyprocessing as p


p.size(400, 400)

def mouseDragged():
	# draw a line between previous and current mouse position
	p.line(p.pmouse.x, p.pmouse.y, p.mouse.x, p.mouse.y)

def keyPressed():
	# clear the screen
	if p.key.char in 'cC':
		p.background(200)

p.run()

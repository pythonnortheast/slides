#!/usr/bin/evn python
# coding=utf-8
"""
Mouse interaction.

"""
import pyprocessing as p

def setup():
	p.size(400, 400)
	p.rectMode(p.CENTER)
	p.noStroke()

def draw():
	p.background(50)  # grey scale
	p.fill(255, 150)  # grey scale + alpha

	size = p.mouse.y / 2
	p.rect(p.mouse.x, 200, size + 10, size + 10)
	p.rect(400 - p.mouse.x, 200, 210 - size, 210 - size)

p.run()

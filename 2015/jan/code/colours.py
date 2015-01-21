#!/usr/bin/evn python
# coding=utf-8
"""
Colours.

"""
import pyprocessing as p

p.size(400, 500)
p.colorMode(p.HSB, 360, 100, 100, 100)
p.background(0, 0, 0)  # HSB

p.fill(120, 50, 50)  # HSB
p.triangle(100, 410, 200, 200, 300, 410)

p.fill(40, 50, 100)  # HSB
p.ellipse(100, 300, 40, 40)
p.ellipse(300, 300, 40, 40)

p.ellipse(200, 180, 190, 200)

p.stroke(10, 100, 75)  # HSB
p.strokeWeight(10)
p.line(183, 246, 245, 230)

p.stroke(100, 50, 100)  # HSB
p.line(107, 163, 295, 163)

p.fill(230, 50, 100, 50)  # HSB + alpha
p.rect(132, 150, 50, 40)
p.rect(215, 150, 50, 40)

p.run()

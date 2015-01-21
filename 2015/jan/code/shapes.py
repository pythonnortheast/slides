#!/usr/bin/evn python
# coding=utf-8
"""
Shapes.

"""
import pyprocessing as p

p.size(400, 500)  # screen width and height

# body
p.triangle(100, 410, 200, 200, 300, 410)  # 3 points (x,y)

# hands
p.ellipse(100, 300, 40, 40)  # centre point (x,y)
p.ellipse(300, 300, 40, 40)  # and size (width,height)

# face
p.ellipse(200, 180, 190, 200)

# mouth
p.line(183, 246, 245, 230)  # 2 points (x,y)

# frames
p.line(107, 163, 295, 163)

# lenses
p.rect(132, 150, 50, 40)  # top left corner (x,y)
p.rect(215, 150, 50, 40)  # and size (width,height)

p.run()

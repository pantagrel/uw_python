import math
#see class notes for how to copy simple objects.

# class Stringy:
# 	def __str__(self):
# 		self = self.__class__
# 		return "%s %s" % self.__class__
# 
# s = Stringy()
# print s.__str__

class Point(object):
	"""Represents a point in 2-D space.
	
	attributes: x, y
	"""

# blank = Point()
# blank.x = 3.0
# blank.y = 4.0
# 
# def distance_between_points(p1, p2):
# 	distance = math.sqrt(p1 ** 2) + (p2 ** 2)
# 	print distance
# 
def print_point(p):
	print '%g, %g' % (p.x, p.y)
# 	
# #distance_between_points(5, 9)

class Rectangle(object):
	"""Represents a rectangle.
	
	attributes: width, height, color, corner.
	"""

box = Rectangle()
# box.x = 20
# box.y = 30
box.width = 100.0
box.height = 200.0

box.corner = Point()
box.corner.x = 4.0
box.corner.y = 8.0  #x and y are embedded attributes

def find_center(rect):
	p = Point()
	p.x = rect.corner.x + rect.width/2.0
	p.y = rect.corner.y + rect.height/2.0
	return p 
# 
# center = find_center(box)
# print_point(center)
# 
# def grow_rectangle(rect, dwidth, dheight):
# 	rect.width += dwidth
# 	rect.height +=dheight
# 
# print box.width, box.height
# grow_rectangle(box, 40, 60)
# print box.width, box.height

#--------------------------------------------------------------------------------
"""
ex.15.2 move a rectangle (rect, dx, dy)
"""


def move_rectangle(rect, dx, dy):
# 	rect.corner = Point()
	rect.corner.x += dx
	rect.corner.y += dy

# print box.corner.x 	
# move_rectangle(box, 36, 77)	
# print box.corner.x, box.corner.y	


#--------------------------------------------------------------------------------
"""
ex.15.3 copying
"""

p1 = Point()
p1.x = 3.0
p1.y = 4.0

import copy
p2 = copy.deepcopy(p1)

# print_point(p2)
# print p1 is p2
# print p1== p2

def move_rectangleCopy(rect, dx, dy):
	rect2 = copy.deepcopy(rect)
	rect2.corner.x += dx
	rect2.corner.y += dy
	return rect2.corner.x, rect2.corner.y, rect2 ==rect 

# print move_rectangleCopy(box, 20, 40)
# print hasattr(box.corner, 'x')
# print type(box)


#--------------------------------------------------------------------------------
"""
ex.15.4 swampy
"""

from swampy.World import World

world = World()
canvas = world.ca(width=500, height=500, background='white')
bbox = [[-150, -100], [150, 100]]
canvas.rectangle(bbox, outline='black', width=2, fill='green4')
canvas.circle([-25, 0], 70, outline=None, fill='red')

world.mainloop()

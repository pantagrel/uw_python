from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print bob


#how many sections?
#which turtle?
#how big are each section's sides?
"""bob goes out, turns, comes back, turns around 180 degrees. repeats 'sides' times
"""


def turtlePie(t, sides, radius):
    circumference = 2 * 3.14 * radius
    length = circumference / sides
    for i in range(sides):
        degrees = 360/sides
        angleAC = 180 - degrees
        angleB = 360 - angleAC * 2
        fd(bob, length)
        lt(bob, degrees)
        fd(bob, radius)
        lt(bob, degrees)
        fd(bob, length)
        lt(bob, 180)



lengthA = 100
lengthB = lengthA * 1.4
degrees = 360/5
angleAC = 180 - degrees
angleB = 360 - angleAC * 2

lt(bob, angleB)
fd(bob, lengthB)
lt(bob, angleAC)
fd(bob, lengthA)
lt(bob, angleAC)
fd(bob, lengthB)


#turtlePie(bob, 5, 50)

wait_for_user()
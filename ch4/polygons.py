from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print bob
bob.delay = 0.01 


def square(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)

def polygon(t, length, n):
    degrees = 360/n
    for i in range(n):
        fd(t, length)
        lt(t, degrees)
        
def circle(t, r):
    circumference = 2 * 3.14 * r
    n = int(circumference/3) + 1
    length = circumference / n
    polygon(t, length, n)


#square(bob, 46)
polygon(bob, 20, 6)
circle(bob, 100)

wait_for_user()
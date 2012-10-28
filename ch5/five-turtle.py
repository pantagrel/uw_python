from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print bob
bob.delay = 0.01

def draw(t, length, n):
#when n gets to 0, exit function
    if n == 0:
        return
#how far to turn in any direction 
    angle = 50
#bob forward initial distance * iterations remaining
    fd(t, length * n)
#bob turn left 'angle' degrees
    lt(t, angle)
#RECURSION: go right, but with counter reduced by 1
#KEEPS GOING FORWARD, BUT ALSO CALLS SECOND SET OF FORWARD MOTIONS
    draw(t, length, n - 1)
#bob right turn at twice angle
#right turns are 2*angle because it's calculating the outside of angle now, unlike left which calculates inside of angle?
    rt(t, 2 * angle)
#RECURSION: go left, but with counter reduced by 1
#KEEPS GOING FORWARD, BUT CALLS THIRD SET OF FORWARD MOTIONS
    draw(t, length, n - 1)
#bob left turn 'angle' degrees
    lt(t, angle)
#bob go backwards basic length * counter    
    bk(t, length * n)
    

#draw(bob, 8, 5) 

def koch(t, length):
    divisor = 3.33
    angle1 = 60
    angle2 = 120
    if length < 3:
        angle = 0
        fd(t, length)
    else:
        koch(t, length/divisor)
        lt(t, angle1)
        koch(t, length/divisor)
        rt(t, angle2)
        koch(t, length/divisor)
        lt(t, angle1)
        koch(t, length/divisor)


def snowflake(t, length, sides):
    for i in range(sides):	
        koch(t, length)
        lt(t, 360/sides)

"""
EXERCISE 5.4, NUMBER 3
DISCUSS HOW TO MAKE VARIATIONS. NOT SURE WHAT TO CHANGE TO MAKE IT LOOK QUATRATIC, ETC. WHAT STRINGS TO PULL?
"""
	
koch(bob, 1550)
#snowflake(bob, 720, 4)
wait_for_user()
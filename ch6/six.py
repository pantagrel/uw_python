import math

def fibonacci(n):
	space = ' ' * (4 * n)
	print space, 'fibonacci', n
	if not isinstance(n, int):
	    print 'only numbers, frenchman!'
	elif n < 0:
	    print 'only positive numbers, frenchman!'
	elif n == 0:
	    print space, 'returning 1'
	    return 0
	elif n == 1:
	    print space, 'returning 0'
	    return 1
	else:
	    print space, 'fibonacci', n
	    return fibonacci(n - 1) + fibonacci(n - 2)

def areaOfCircle(radius):
    return math.pi * radius**2

def distance(x1, x2, y1, y2):
    dx = x2 - x1
    dy = y2 - y1
    return math.sqrt(dx**2 + dy**2)

def circle_area(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    #print areaOfCircle(radius)
    return areaOfCircle(radius)

circle_area(45, 6, 78, 90)
areaOfCircle(50)
distance(3, 4, 6, 9)


def ackerman(m, n):
    if m == 0:
        n + 1
    elif m > 0 and n == 0:
        (m - 1, 1)
    elif m > 0 and n > 0:
        (m - 1)
        (m, n - 1)
    else:
        return 'monkeypants'


def first(word):
    print word[0]
    return word[0]

def last(word):
    print word[-1]
    return word[-1]

def middle(word):
    print middle[1: -1]
    return word[1:-1]

print fibonacci(5)
#ackerman(3, 4)
#first('')
#last(" ")
#middle('mississipspi')
def plus(a, b):
    print a, b*4, a, b*4, a, b*4, a, b*4, a

def interior(c, d):
    print c, d*4, c, d*4, c, d*4, c, d*4, c

def interior2(c, d):
    interior(c,d)
    interior(c,d)

#interior2 works but not interior4. says interior4 is not defined...changed name to 'fourTimes' and it started working!!???
def fourTimes(c, d):
    interior2(c, d)
    interior2(c, d)

def block(a, b, c, d):
    plus(a,b)
    fourTimes(c,d)

def blockTwice(a, b, c, d):
    block(a, b, c, d)
    block(a, b, c, d)

def blockFour(a,b,c,d):
	blockTwice(a, b, c, d)
	blockTwice(a,b,c,d)
	plus(a,b)


#block('+', '-', '|', ' ')

blockFour('+ ', '- ', '| ', '  ')


#recursion
def countdown(n, s):
    if n < s:
        print 'blastoff!'
    else:
        print n
        countdown(n-1)

def askName():
    name = raw_input('what is your name?\n')
    print 'nice to meet you, ' + name

def askNumber():
    prompt = raw_input('what is your vector, victor?\n')
    speed = int(prompt)
    print speed, type(speed)

def check_fermat(a, b, c, n):
    '''
1. try this so the user can input values into terminal.
'''
    if ((a ** n + b ** n)==c ** n) and (n > 2):
        print 'fermat wrong!'
    else:
        print 'fermat correct so far.' 

def loopers():
	n = 10
	while n > 0:
	    print n
	    n = n - 1
	    
loopers()

def check_fermat_input():
    """
can the first (getting input section) part be a loop? 
and each part of loop is stored in a different variable?

    x = 4
    while x > 0:
        #ask for input
"""

    a = int(raw_input('please enter value #1: \n > '))
    b = int(raw_input('please enter value #2: \n > '))
    c = int(raw_input('please enter value #3: \n > '))
    n = int(raw_input('please enter the exponential value: \n > '))
    if ((a ** n + b ** n)==c ** n) and (n > 2):
        print 'fermat wrong!'
    else:
        print 'computing............'
        print '.....................'
        print '............analysis:'
        print 'Fermat correct so far.' 

def is_triangle(a, b, c):
    if (a + b) < c:
        print 'not a triangle.'
    else:
        print 'good job!'

def user_triangle():
    prompt = 'gimme some digits, three times.\n'
    a = int(raw_input('first side length:\n> '))
    b = int(raw_input('second side length:\n> '))
    c = int(raw_input('third side length:\n> '))
    is_triangle(a, b, c)

#askName()
#countdown(10, 0)
#askNumber()
#check_fermat(13, 29, 41, 7)
#check_fermat_input()
#is_triangle(5, 2, 1)
user_triangle()

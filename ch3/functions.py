#exercise 3.3
'''
def right_justify(word):
    leadingSpace = 70 - len(word)
    rightWiseWord = (leadingSpace * ' ') + word
    print rightWiseWord
'''
def do_twice(f):
    f()
    f()

def print_spam():
	print 'spam'

def print_twice(word):
    print word
    print word

def do_twice_2(f, v):
	f(v)
	f(v)

def do_four(f, v):
    print_twice(v)
    print_twice(v)

do_twice(print_spam)
#do_twice_2 needs to call a function that takes arguments???
do_twice_2(print_twice, 'fucking python')
do_four(print_twice, 'house') #why do i call print_twice in the definition as well as here?



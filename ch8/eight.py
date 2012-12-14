#-------------------------------------------------------------
# ex. 8.1
#function that takes string as arg and displays string backwards, one item per line.
def reverser(str):
    index = len(str) - 1
    while index >= 0:
        letter = str[index]
        print letter,
        index = index - 1
#reverser('gadzooks')

#-------------------------------------------------------------
#ex. 8.1.2
#traversal of a string with a for loop:
def charTest(str):
    for char in str:
        print char
#charTest('banana')
    
#-------------------------------------------------------------
#ex. 8.2
#abecedarian sequence. using concatenation to build new strings:

def jackQuack():
	prefixes = 'JKLMNOPQ'
	suffix = 'ack'
	altSuffix = 'uack'
	for letter in prefixes:
	    if letter == 'O' or letter == 'Q':
	        print letter + altSuffix
	    else:
	        print letter + suffix

#jackQuack()

#-------------------------------------------------------------

# r = raw_input('enter a word at least 5 letters long\n> ')
# print r[0:4]
# print "'" + r[4:] + "' is the rest of the string"

# s = "monty python"
# #this prints the whole string
# print s[:]

# #strings are immutable, but can be variables resassigned
# hi = 'hello'
# newHi = 'J' + hi[1:]
# print hi
# print newHi
# 

#-------------------------------------------------------------
def traversal(letter, word):
	"""looks for a character within a string, returns how many of character. if char not found, return 'char not found' """
	counter = 0
	for character in word:
		if character == letter:
			counter += 1
	if counter == 0:
		print 'char not found'
	else:
		print counter

#traversal('a', 'bananananananan')


#ALT: LETTER POSITION INSTEAD OF LETTER COUNT
def traversalIndex(letter, word):
	"""looks for a character within a string, returns index of all characters. if char not found, return 'char not found' """
	index = 0
	letterOutput = []
	while index < len(word):
		letterChecker = word[index]
		if letterChecker == letter:
			#put that letter in a str:
			letterOutput.append(index)
		index += 1
	if letterOutput == []:
		print 'char not found'
	else:
		print letterOutput

#traversalIndex('X', 'bananananananan')


#-------------------------------------------------------------
#ex. 8.4
def find(word, letter, start):
	"""looks for first instance of a letter within in a word. returns that index if found, else returns -1"""
	index = start
	while index < len(word):
		if word[index] == letter:
	    		return index
	    	index = index + 1
	return -1

# s = find('yellow', 'l', 5)
# print s

#-------------------------------------------------------------
#ex. 8.5
#counts number of instances of a letter within a string:
def letterCounter(word, whichLetter):
    count = 0
    for letter in word:
        if letter == whichLetter:
            count = count + 1
    print count

#letterCounter('respectinge', 'e')

#-------------------------------------------------------------
#ex. 8.6
#repeat ex. 8.5, but use the find() function for ex. 8.4

def letterCounterModified(word, whichLetter='', start=0):
    return find(word, whichLetter, start)    
    
        
#print letterCounterModified('rapscallion roger davis', 'r', 2)

#-------------------------------------------------------------
word = 'baNAnaXXX'
new_word = word.lower()
#print new_word
index = new_word.count('x')
#print index


#-------------------------------------------------------------
#ex. 8.7, ex. 8.8
"""explore pythong string documentation. play around."""
fruit = 'banana'
state = "Mississippi"
veggie = 'zucchini'
dog = "dachshund"
cat = "Siamese"
house = "craftsman houses are nice looking. there are quite a few in seattle."

#print dog.count('s')
#print house.upper()
#print house[::-1]
#print house.replace('are', 'fuck')
#print 'www.example.com'.strip('cmowz.')
def inBoth(word1, word2):
	for letter in word1:
		if letter in word2:
			print letter	

#print inBoth('apples', 'oranges')


#-------------------------------------------------------------
#ex.8.9
#find the error in the reverse function in the book:




#-------------------------------------------------------------
#ex 8.10
def is_palindrome(word):
    return word[::1] == word[::-1]

def is_reverseWord(word1, word2):
	return word1[::1] == word2[::-1]
	    
print is_palindrome('amanaplanacanalpanama')
print is_reverseWord('stop', 'pots')

#-------------------------------------------------------------
#ex 8.11
#describe whate wrong with the following functions:

#***********
#this one: only checks the first letter?
#***********
def is_lower(s):
    for c in s: #what is with this variable name??? like 'i'? can be any old letter?
        if c.islower():
            return True
        else:
            return False
            
#print is_lower('banAna')

#***********
#this one just checks the string 'c'
#***********
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
            
#print any_lowercase2('pine')

#*********
#'flag' get T/F value for each char. this function only return the last value of flag, so if last letter is lowercase, the function will return true.
#should be a return line for the first instance of finding an upper
#*********
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
        print c
        if flag == False:
            return False
    else:    
        return True
#modified function 4 to be like function 5, which is the only function that works: actually checks the whole string.
	
#print any_lowercase3('houseDDDDaF')

#-------------------------------------------------------------
#ex. 8.12
#ROT13 weak encryption
import math

def rotate_word(word, rotateInt):
    newWord = ''
    letterCode = 0
    for c in word:
        letterCode = ord(c) + int(rotateInt)
        if letterCode > 122:
            letterCode = 96 + (letterCode - 122)
        elif letterCode < 97:
            letterCode = 121 + (rotateInt - (letterCode - 97))
        # elif letterCode < 97 and letterCode > 90:
#             letterCode = 71 + (letterCode - 97)
        newWord = newWord + chr(letterCode)
    return newWord

#SOLVE FOR BIG NUMBERS: CREATE A '360' SYSTEM: divide by num to get a set point on a circle?    
#print rotate_word("watermelon", -150)

#-------------------------------------------------------------


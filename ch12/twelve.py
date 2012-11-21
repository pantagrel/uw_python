#import sys
import random
#sys.path.append()
#import structshape.py
"""
QUESTIONS:
1. split a variable into separate variables: splitting an email address, e.g.: how to send that data to a dictionary or a list? E.g.: lots of emails, would like to organize by either username or domain.
"""


#--------------------------------------------------------------------------------
"""
ex. 12.1: 'sumall': takes any number of args and returns their sum
"""

def sumall(*args):
	adder = 0
	for i in range(len(args)):
		adder = adder + args[i]
	return adder
	

#--------------------------------------------------------------------------------
"""
ex. 12.2	
sort words in order by length. words of same length sorted randomly (not alpha)
"""

def sortKindaRandom(lst):
	fin = open(lst)
	t = []
	for line in fin:
		randomiZr = random.random()
		word = line.strip()
		t.append((len(word), randomiZr, word))
# 		print t 	
	t.sort(reverse=False)
	t1 = []	
	for length, randomiZr, word, in t:
		if length > 3 and length < 5:
			t1.append(word)
	return t1


#--------------------------------------------------------------------------------
"""
ex. 12.3: print the letters of a string in decreasing order of frequency
***************** works, but CAN'T FIGURE OUT HOW TO NOT COUNT SPACES/PUNCTUATION
****************************getting key errors for commented out area.
"""

def letterCount(s):
	d = dict()
	for c in s:
		# if c == ' ':
# 			d[c] = d[c]
# 		elif c == '.':
# 			d[c] += 0
		if c not in d:
			d[c] = 1
		else:
			d[c] += 1
	return d

def histogram(d):
	l = []
	for k in d:
		l.append((d[k], k))	
	l.sort(reverse = True)
	return l 
	

#--------------------------------------------------------------------------------
"""
ex. 12.4: read words from a set. print out all the sets of words that are anagrams.

leftover/later use code: add words to list, zip, organize based on line length:
words = []
	wordLen = []
	for line in fin:
		words.append(line.strip())
		wordLen.append(len(line.strip()))
	#zippedList = zip(wordLen, words)
	#zippedList.sort()
"""

#takes a file of words and organizes into a list of [(word length, word)].

def listOrganizer(file):
	fin = open(file)
	d = dict()
	wordLen = 0
	for line in fin:
		word = line.strip()
		tupleWord = tuple(word)
#HOW CAN I COMPARE TUPLE-KEYS? GETTING A KEY ERROR WHEN I TRY TO COMPARE (==)		
		if tupleWord not in d:
			d[tupleWord] = word
		else:
			d[tupleWord] = 1
	print d	
	
# def anagrams(file):
# 	listOrganizer(file)
	 

#--------------------------------------------------------------------------------
	
if __name__ == "__main__":
	s = 'n'
# 	print 'ex 12.1:', sumall(1,2,3,4,5,6,7,3,4,2)
#	print 'ex 12.2:', sortKindaRandom('words.txt')
	#histy = letterCount(s)
	#print histogram(histy)
	#print anagrams('words2.txt')
	listOrganizer('words2.txt')
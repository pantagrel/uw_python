
from random import randint 
import time


emptyList = []
cheeseList = ['Edam', 'brie', 'chevre', 'mozzarella', 'feta', 'Swiss', 'ricotta']
meatList = ['shrimp', 'bacon', 'tongue']
veggieList = ['broccoli', 'beans', 'lettuce', 'kale', 'onions', 'cucumber', 'cucumber', 'cilantro', 'carrot', 'cauliflower', 'carrot']
groceries = [cheeseList, meatList, veggieList]

def randomListMaker():
    t = []
    listLength = randint(5, 100)
    i = 0
    while i < listLength:
        t.append(randint(0, 1000))
        i += 1
    return t 
    
# print randomListMaker() 

#print 'Edam' in cheeses
#print 'Brie' in cheeses
# for owls in cheeses: #the variable after 'for' can be anything legal
#   print owls

# for cheeseType in range(len(cheeseList)): 
#   cheeseList[cheeseType] = (cheeseList[cheeseType] + ' ' )* 4
#   print cheeseList[cheeseType]

#print groceries + groceries


#--------------------------------------------------------------------------------
# ex. 10.1 
"""
sum of nested list of integers. in this method, all list elements should be lists
in this method, one must know how many levels of nesting is happing (for the 
'for loops')
"""

listOne = [2, 4, 6, 8]
listTwo = [1, 3, 5, 7]
list3 = [listOne, listTwo, [8, 9, 10, 11]]

def nested_sum(theList):
	listSum = 0
	for x in theList:
		for y in x:
			listSum += y 
	return listSum
    
# print nested_sum(list3)


#--------------------------------------------------------------------------------
# ex. 10.1 
"""
sum of nested list of integers. in this method, all list elements should be lists
in this method, one must know how many levels of nesting is happing (for the 
'for loops')
"""

listThree = [listOne, listTwo, 8, 9, 10, 11]

def nested_sumNestMix(theList):
	listSum = 0
	for x in theList:
		if type(x) == list:
			for y in x:
				listSum += y
		else:
			listSum += x
	return listSum
    
# print nested_sumNestMix(listThree)


#--------------------------------------------------------------------------------
#ex. 10.2 
"""
take a list of nested strings, return a nested list with all strings capitalized.
"""

def capitalize_all(t):
res = []
	for s in t:
		subRes = []
		for u in s:
			subRes.append(u.capitalize())
		res.append(subRes)
	return res

# print capitalize_all(groceries)


#--------------------------------------------------------------------------------
# ex. 10.3
"""
cumulative sum of a list of integers
"""

def cumulative_sum(t):
	newList = t[:]  #comment this line out, changes vars to 't' and the original list will be modified instead of a new list
	holder = 0    
	for i in range(len(t)):
		holder += t[i] 
		newList[i] = holder
	return newList
    
#print cumulative_sum(listOne)    


#--------------------------------------------------------------------------------
#ex. 10.4
"""
return all but first and last elements
"""

def middle(t):
	if len(t) > 2:
		s = t[1:-1]
		return s 
	else:
		return 'short list! come back with a longer one.'

# print middle(meatList)


#--------------------------------------------------------------------------------
# ex. 10.5
"""
remove first and last, return none
"""

def chop(t):
	del t[1]
	del t[-1]
	print t
	return None 

# chop(cheeseList)
# print cheeseList

#--------------------------------------------------------------------------------
# ex. 10.6
"""
list as a parameter and returns True if the list is sorted in ascending order and False otherwise. You can assume (as a precondition) that the elements of the list can be compared with the relational operators <, >, etc.
"""


def is_sorted(t):
	i = 1
	while i < len(t):
	#print 'i is ', i
		if t[i-1] <= t[i]:
# 			print t[i]
			i += 1
		else:
			return False
	return True


# cheeseList.sort()
# print is_sorted(cheeseList) 


#--------------------------------------------------------------------------------
# ex. 10.7
"""
words are anagrams if you can rearrange the letters from one to spell the other. Write a function called is_anagram that takes two strings and returns True if they are anagrams.
"""


def is_anagram(string1, string2):
	tStr1 = list(string1)
	tStr2 = list(string2)
	tStr1.sort()
	tStr2.sort()
	if tStr1 == tStr2:
		print "'%s' and '%s' are anagrams" % (string1, string2)
		return True
	else:
		print 'NOT A MATCH:', string1, string2
		return False

# is_anagram('salt', 'alts')


#--------------------------------------------------------------------------------
# ex. 10.8.1
"""
takes a list and returns if there are multiples of a list element
ONLY RETURNS FIRST DUPLICATE INSTANCE
"""

def has_duplicates(t):
	newList = t[:]
	newList.sort()
	#print newList
	for i in range(len(newList)-1):
		if newList[i] == newList[i-1]:
			#print newList[i], '>> Positions', i, 'and', i-1, 'are duplicates.'
			return True
	return False

# print has_duplicates(veggieList)

#--------------------------------------------------------------------------------
# ex. 10.8.2
"""
If there are 23 students in your class, what are the chances that two of you have the same birthday? You can estimate this probability by generating random samples of 23 birthdays and checking for matches. Hint: you can generate random birthdays with the randint function in the random module.
"""

def birthdayParadox(numOfStudents):
	t = []
	i = 0
	while i < numOfStudents:
		#print i
		t.append(randint(0, 365))
		i += 1
	return has_duplicates(t)
    
    
def run_birthdayParadox(numOfStudents, numOfCycles):
	percentageDuplicates = 0.0
	i = 0
	while i < numOfCycles:
		if birthdayParadox(numOfStudents) == True:
			percentageDuplicates +=1.0
			i += 1
		else:
			i += 1
	percentageDuplicates = (percentageDuplicates/numOfCycles) * 100
	print "%f percent of the cycles run have duplicates." % percentageDuplicates
    
# print birthdayParadox(23)
####when numOfStudents changes from 23 to 32, the % duplicates goes from 50% to 70%
# run_birthdayParadox(35, 10000)

#--------------------------------------------------------------------------------
# ex. 10.9
"""
Take a list and return a new list with only the unique elements from the original. Hint: list doesnt have to be in the same order.
"""


def remove_duplicates(t): 
	newList = t[:]
	newList.sort()
	finalList = []
	i = 0
	while i < len(newList):
		if newList[i] != newList[i-1]:
			print i
			finalList.append(newList[i])
		i += 1
	return finalList

# testList = randomListMaker()
# print remove_duplicates(veggieList)


#--------------------------------------------------------------------------------
# ex. 10.10
"""
Write a function that reads the file words.txt and builds a list with one element per word. Write two versions of this function, one using the append method and the other using the idiom t = t + [x]. Which one takes longer to run? Why?
"""

def wordListAppend(file):
	t1 = time.time()
	wordList = []
	fin = open(file)
	for line in fin:
		word = line.strip()
		wordList.append(word)
	t2 = time.time() - t1
	print t2, ' append method'
	return wordList
    
def wordListIncrementer(file):
	t1 = time.time()
	wordList = []
	fin = open(file)
	for line in fin:
		word = line.strip()
		wordList = wordList + [word]
	t2 = time.time() - t1
	print t2, ' += method'
	return wordList

#USE .append(x) TO ADD ELEMENTS TO STRINGS:
# wordListAppend('words.txt')
 
#increment is WAY WAY WAY slower.
# wordListIncrementer('words.txt')        

#--------------------------------------------------------------------------------
# ex. 10.11
################### NOT DONE
"""
To check whether a word is in the word list, you could use the in operator, but it would be slow because it searches through the words in order.
Because the words are in alphabetical order, we can speed things up with a bisection search (also known as binary search), which is similar to what you do when you look a word up in the dictionary.

You start in the middle and check to see whether the word you are looking for comes before the word in the middle of the list. If so, then you search the first half of the list the same way. Otherwise you search the second half.
Either way, you cut the remaining search space in half. If the word list has 113,809 words, it will take about 17 steps to find the word or conclude that it’s not there.
Write a function called bisect that takes a sorted list and a target value and returns the index of the value in the list, if it’s there, or None if it’s not.
Or you could read the documentation of the bisect module and use that! Solution: http:// thinkpython.com/code/inlist.py
"""

def bisect(targetWord):
	fin = open('words.txt')
	tempList = []
	length = len(tempList)
	for line in fin:
	    word = line.strip()
	    tempList.append(word)
	#if the word is exactly in the middle, first try:
	if targetWord == tempList[length/2]:
		return tempList[length/2]
	elif targetWord > tempList[length/2]:
		bisect(targetWord)
	elif targetWord < tempList[length/2]:
		bisect(targetWord)
	elif targetWord == tempList[i]:
		return i
	else:
		return None	
			
print bisect('zebra')


#--------------------------------------------------------------------------------
# ex. 10.12
################### NOT DONE
"""
Two words are a “reverse pair” if each is the reverse of the other. Write a program that finds all the reverse pairs in the word list. 
"""

def checkWord(word1, word2):
	if len(word1) == len(word2):
		if word1[:1] == word2[-1:]:
			checkWord(word1, word2)
# 			return word1, word2
	else
		return None	

def reversePairs(wordList): 
    fin = open(wordList)
    pairsList = []
    for line in fin:
    	word = line.strip()
    	tempList.append(word)
    i = 0
    while i < len(tempList):
    	tempList[i] = word1 
    	tempList[i - 1] = word2
    	currentTest = checkWord(word1, word2)
    	if currentTest != None:
    		pairsList.append(currentTest)
    	i += 1
    	
#     	if word[::1] == nextWord[::-1]:
#     		word.append(pairsList)
#     		nextWord.append(pairsList)

#--------------------------------------------------------------------------------
# ex. 10.13
################### NOT DONE
"""
Exercise 10.13. Two words “interlock” if taking alternating letters from each forms a new word. For example, “shoe” and “cold” interlock to form “schooled.” 
"""

def interlockingWords(file):
    return None

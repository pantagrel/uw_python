#PRACTICE
#empty list

from random import randint 
import time


emptyList = []
cheeseList = ['Edam', 'Cheddar', 'Gouda', 'mozzarella', 'feta', 'Swiss', 'Laughing Cow']
meatList = ['shrimp', 'bacon', 'tongue']
veggieList = ['broccoli', 'beans', 'lettuce', 'kale', 'onions', 'cucumber', 'cucumber']
groceries = [cheeseList, meatList, veggieList]

def randomListMaker():
    t = []
    listLength = randint(5, 100)
    i = 0
    while i < listLength:
        t.append(randint(0, 1000))
        i += 1
    return t 
    
#print randomListMaker() 

#print 'Edam' in cheeses
#print 'Brie' in cheeses
# for owls in cheeses: #the variable after 'for' can be anything legal
#   print owls

# for cheeseType in range(len(cheeseList)): 
#   cheeseList[cheeseType] = (cheeseList[cheeseType] + ' ' )* 4
#   print cheeseList[cheeseType]

#print groceries + groceries


#--------------------------------------------------------------------------------
"""
ex. 10.1 

sum of nested list of integers. in this method, all list elements should be lists
in this method, one must know how many levels of nesting is happing (for the 
'for loops')
"""
listOne = [2, 4, 6, 8]
listTwo = [1, 3, 5, 7]
listThree = [listOne, listTwo, [8, 9, 10, 11]]

def nested_sum(theList):
  listSum = 0
  for x in theList:
    for y in x:
      listSum += y 
  return listSum
    
#print 'ex. 10.1\n', nested_sum(listThree)


#--------------------------------------------------------------------------------
"""
ex. 10.2 
take a list of nested strings, return a nested list with all strings capitalized.
"""

def capitalize_all(t):
  res = []
  subRes = []
  for s in t:
    for u in s:
      subRes.append(u.capitalize())
  res += subRes  
  return res

#print 'ex 10.2\n', capitalize_all(groceries)


#--------------------------------------------------------------------------------
"""
ex. 10.3
cumulative sum of a list of integers
"""

def cumulative_sum(t):
  newList = t[:]  #comment this line out, changes vars to 't' and the original list will be modified instead of a new list
  holder = 0    
  for i in range(len(t)):
    holder += t[i] 
    newList[i] = holder
  return newList
    
#print 'ex. 10.3\n', cumulative_sum(listOne)    


#--------------------------------------------------------------------------------
"""
ex. 10.4
return all but first and last elements
"""


def middle(t):
  if len(t) > 2:
    s = t[:]
    return s[1:-1]
  else:
    return 'short list! come back with a longer one.'

#print 'ex. 10.4\n', middle(meatList)


#--------------------------------------------------------------------------------
"""
ex. 10.5
remove first and last, return none
"""

def chop(t):
  del t[1]
  del t[-1]
  #print t
  return None 

# chop(cheeseList)
# print 'ex. 10.5\n', cheeseList

#--------------------------------------------------------------------------------
"""
ex. 10.6
return True is a list is sorted in ascending order
"""

def is_sortedXXXXX(t):
    for i in range(len(t)-1):
        if t[i] > t[i-1]:
            print t[i]
            return False
        print t[i]
        #return True
     
#try a while loop? 
def is_sorted(t):
    i = 1
    while i < len(t):
        #print 'i is ', i
        if t[i-1] < t[i]:
            #print t[i]
            i += 1
        else:
            #print t[i-1], ' ', t[i]  #show the two that are the first in list to 
            #be out of order
            return False
    return True


#cheeseList.sort()
#print 'ex. 10.6\n', is_sorted(["apples", "brie", "carleton", 'dog', 'dagger', 'knock']) 


#--------------------------------------------------------------------------------
"""
ex. 10.7: check to see if two word are anagrams of each other,assuming whatever 
input comes in are both real words

"""

def is_anagram(string1, string2):
    tStr1 = list(string1)
    tStr2 = list(string2)
    tStr1.sort()
    tStr2.sort()
    if tStr1 == tStr2:
        print string1, string2, 'are anagrams'
        return True
    else:
       	print 'NOT A MATCH:', string1, string2
        return False

#is_anagram('goose', 'sss')


#--------------------------------------------------------------------------------
"""
ex. 10.8.1: takes a list and returns if there are multiples of a list element
*******************************this only returns the first duplicate instance
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

#print has_duplicates(veggieList)

#--------------------------------------------------------------------------------
"""
ex. 10.8.2 : birthday paradox. 23 students. try using 'randint' from 'random' 
module
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
    print percentageDuplicates, '% of the cycles run have duplicates.'
    
#print birthdayParadox(23)
#when numOfStudents changes from 23 to 32, the % duplicates goes from 50% to 70%
#run_birthdayParadox(32, 10000)

#--------------------------------------------------------------------------------
"""
ex. 10.9: get a list, return new list with only unique elements

******************** NOT DONE. PROBLEM: list index out of range. when list items 
are removed it affects the len value and throws an error

"""
#try building a new list with those duplicate values
# for item in tempList, remove item in 

def remove_duplicates(t): 
    newList = t[:]
    newList.sort()   #try 'sorted'. creats new list, leaves original alone
    for i in range(len(newList) - 1):
        tempList = 0
        if newList[i] == newList[i-1]:
            #print 'Item', newList[i], 'was removed.'
            tempList += [i]
            #del newList[tempList]
    return tempList

#testList = randomListMaker()
#print remove_duplicates(testList)


#--------------------------------------------------------------------------------
"""
ex. 10.10: read 'word.txt' file, build list with one element per word.
write two versions, compare time: one with .append() and one with t = t + [x]
use 'time' module to measure elapsed time
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
#wordListAppend('words.txt')
 
#increment is WAY WAY WAY slower.
#wordListIncrementer('words.txt')        

#--------------------------------------------------------------------------------
"""
ex. 10.11: use a bisection method to look for a word in the word list. 
input a word. return index of word in list or NONE if it's not there.
there is a 'bisect' module. read the documentation. try this after the recursion way.
"""

def bisect(targetWord, wordList):
	fin = open(wordList)
	tempList = []
	for line in fin:
	    word = line.strip()
	    tempList.append(word)
	list_length = len(tempList)
	if list_length == 1:
		if targetWord == tempWord[0]:
			return 0
		else:
			return None
			
	#STUCK. HOW TO DO THE RECURSIVE CALLS.
	
 	return list_length
	# go to middle of list. if word is here, done
	#if word is >, go to middle of >
	#if word is <, to to middle of <

#--------------------------------------------------------------------------------
"""
ex. 10.12: find all the reverse pairs in the word list
"""
def reversePairs(file): 
    print None 

#--------------------------------------------------------------------------------
"""
ex. 10.13: find all the 'interlocking' words: 'shoe' + 'cold' = 'schooled'
"""
def interlockingWords(file):
    return None
    
if __name__ == "__main__":
	#bisect('baby', 'words2.txt')
import string 

# print string.punctuation
# print string.whitespace

#--------------------------------------------------------------------------------
#ex. 13.1

"""
Write a program that reads a file, breaks each line into words, strips whitespace and punctuation from the words, and converts them to lowercase.
Hint: The string module provides strings named whitespace, which contains space, tab, newline, etc., and punctuation which contains the punctuation characters. 
"""

def documentStripper(f):
	fin = open(f)
	d = dict()
	wordList = []
	for chunk in fin:
		wordList = chunk.split(' ')
		wordList.sort()
		#insert something here to remove interior punctuation (--, e.g.)
		for w in wordList:
			word = w.strip(string.punctuation)
			word = word.strip(string.whitespace)
			word = word.strip('\xe2\x80\x9c')
			word = word.strip('\xe2\x80\x9d')
# 			word = word.strip('htp')
			word = word.lower()
			if word != "":
				word = word.strip(string.punctuation)
				d[word] = d.get(word, 0) + 1
# 				print "%r" % word
# 				print word
	return d

# print documentStripper('huckFinn.txt')


#--------------------------------------------------------------------------------
#ex. 13.2

"""
Modify your program from the previous exercise to read the book you downloaded, skip over the header information at the beginning of the file, and process the rest of the words as before.
Then modify the program to count the total number of words in the book, and the number of times each word is used.
Print the number of different words used in the book. Compare different books by different authors, written in different eras. Which author uses the most extensive vocabulary? 
"""

def wordCounter(f):
	wordDict = documentStripper(f)
	wordCounter = 0
	lengthGauge = 0
	longestWord = ""
	totalWords = 0
	for k in wordDict:
		totalWords += wordDict[k]
		wordCounter += 1
		if len(k) > lengthGauge:
			lengthGauge += 1
			longestWord = k
# 	print "Total words: %d. %d different words used in %s. The longest word is %s" % (totalWords, wordCounter, f, longestWord) 
	return wordDict
# 	(totalWords, wordCounter, longestWord, wordDict)

# print wordCounter('anneGreenGables.txt')


#--------------------------------------------------------------------------------
#ex. 13.3.1

"""
Modify the program from the previous exercise to print the most frequently-used words in the book.
"""

def topWords(f):
	d = wordCounter(f)
	mostWord = ''
	counter = 0
	wordList 
	for k in d:
		if d[k] > counter:
			mostWord, counter = k, d[k]
			print counter, mostWord
# 		i+=1
	return counter, mostWord
	
# print 'moby', topWords('mobyDick.txt')
# print 'ulysses', topTwentyWords('ulysses.txt')
# print 'anne', topTwentyWords('anneGreenGables.txt')
# print 'huck', topTwentyWords('huckFinn.txt')
# print 'david', topTwentyWords('davidCopperfield.txt')

#--------------------------------------------------------------------------------
#ex. 13.3.2

"""
Modify the program from the previous exercise to print the 20 most frequently-used words in the book. words used singly and still in the list are the most recently used single instances(lowest in alpha order)
"""

# list all
# sort all
# remove all except last 20
# zip

def topTwentyWords(f):
	d = wordCounter(f)
	mostWord = ''
	counter = 0
	wordListCombo = []
	wordList = []
	for k in d:
		if len(wordList) <=20:
			if '--' not in k:
				wordListCombo.append((k, d[k]))
				wordList.append(k)
		if d[k] > counter:
			if '--' not in k:
				mostWord, counter = k, d[k]
				wordListCombo.pop()
				wordList.pop()
				wordListCombo.insert(0,(k, d[k]))
				wordList.insert(0, k)
# 				print "COUNTER/MOST WORD:", counter, mostWord
	return wordList	
	
print topTwentyWords('davidCopperfield.txt')


#--------------------------------------------------------------------------------
#ex. 13.4
"""
Modify the previous program to read a word list (see Section 9.1) and then print all the words in the book that are not in the word list. How many of them are typos? How many of them are common words that should be in the word list, and how many of them are really obscure?
"""
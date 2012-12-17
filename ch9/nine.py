import urllib
#-------------------------------------------------------------
fin = open('words.txt')
# print fin.readline()


#-------------------------------------------------------------
#ex. 9.1
def print_longWords(file):
	"""only print a word if it has more than 20 characters"""
	fin = open(file)
	for line in fin:
		word = line.strip()
		if len(word) > 20:
			print word

# print_longWords('words.txt')

#-------------------------------------------------------------
#ex. 9.2
def has_no_e(file):
	"""only print words that have no 'e' """
	fin = open(file)
	for line in fin:
		word = line.strip()
		if 'e' not in word:
			print word
      
# has_no_e('words.txt')      

#-------------------------------------------------------------
#ex. 9.2.2
def has_no_ePercentage(file):
	"""compute percentage of words in 'words.txt' that have no 'e' """
	counter_total = 0.00
	counter_no_e = 0.00
	fin = open(file)
	for line in fin:
		counter_total = counter_total + 1
		word = line.strip()
		if 'e' not in word:
			counter_no_e = counter_no_e + 1
	print round((counter_no_e/counter_total * 100),2), "percent of words have no 'e'"

# has_no_ePercentage('words.txt')

#-------------------------------------------------------------
#ex. 9.3
# takes str + forbidden letters, returns True if letters aren't there
def avoids(word, str):
	""" takes a word and a string of forbidden letters, and that returns True if the word does not use any of the forbidden letters """
	checker_var = True 
	for char in str:
		if char in word:
			print char
			checker_var = False
	return checker_var
    
# print avoids('i am flhying on a cloud of baro', 'ycl')

#-------------------------------------------------------------
#ex. 9.3.2
def avoids_list():
	""" user inputs forbidden str, checks agains words.txt. prints number of words that do not contain the forbidden str """
	counter = 0
	counter_total = 0
	fin = open('words.txt')
	forbiddenString = raw_input('enter the forbidden letters:\n> ') 
	for line in fin:
		counter_total += 1
		word = line.strip()
		if forbiddenString in word:
			counter += 1
			print word
	print counter_total - counter, 'words do not contain "%s"' % forbiddenString
  
# avoids_list()

#changing 'print' to 'return' in line 75 causes the statement to print in parenthesis with the quotes around the string still showing. why?

#-------------------------------------------------------------
#ex. 9.4
def uses_only(word, letterString):
	""" 
	takes a word and a string of letters, and returns True if the word contains only letters in the list. Can you make a sentence using only the letters acefhlo? Other than 'Hoe alfalfa?' 
	"""
	for letter in word:
		if letter not in letterString:
			return False
#  		print letter
 	return True

# print uses_only('moocheshcesoooooomeschmoooeszzzzzzzza', 'chesomxyz')


#-------------------------------------------------------------
#ex. 9.5.1
def uses_all(word, requiredLetters):
	""" 
	takes a word and a string of required letters, and that returns True if the word uses all the required letters at least once. How many words are there that use all the vowels aeiou? How about aeiouy? 
	"""
	for letter in requiredLetters:
		if letter not in word:
			print letter
			return False
	return True
  
# print uses_all('cows in the field, dogs in the barn, upstairs', 'aeiou')

#-------------------------------------------------------------
#ex. 9.5.2
def uses_allList(requiredLetters):
	""" 
	takes words.txt and a string of required letters: how many words are there that use all the vowels aeiou? How about aeiouy? 
	"""
	counter_not = 0
	counter_total = 0
	fin = open('words.txt')
	for line in fin:
		word = line.strip()
		counter_total += 1
		for letter in requiredLetters:
			if letter not in word:
				break
			counter_not += 1
	return counter_total - counter_not
  
# print uses_allList('aeiouy')

#-------------------------------------------------------------
#ex. 9.6.1
def is_abecedarian(word):
	"""
	returns True if the letters in a word appear in alphabetical order (double letters are ok). How many abecedarian words are there?
	"""
	holder = 'a'
	for letter in word:
		holderNext = letter
		if holderNext >= holder:
			holder = letter
# 			print holder, holderNext
		else:
			return False
	return True
		
# print is_abecedarian('shoots')


#-------------------------------------------------------------
#ex. 9.6.2
#scans words.txt for abecedarian words
def abecedarianList(textFile):
	"""
	returns True if the letters in a word appear in alphabetical order (double letters are ok). How many abecedarian words are there?
	"""
	longestWords = []
	abecedarian_words = 0
	wordLength = 0
	fin = open(textFile)
	for line in fin:
		word = line.strip()	
		i = 0
		while i < len(word) - 1:
			if word[i + 1] >= word[i]:
# 				print word[i]
				i += 1
				if i == len(word) - 1:
# 					print word
					abecedarian_words += 1
# 					record longest abecedarian word
# 					doesnot capture all longets words, but only first one
					if len(word) >= wordLength:
						longestWords.append(word)
# 						print longestWords
# 						print wordLength, word
						wordLength = len(word)			
			else:
				break
	return abecedarian_words
	
# print abecedarianList('words.txt')

#-------------------------------------------------------------
#ex. 9.7
def threeDoubles(file):
	"""
	find a word that has 3 double letters
	"""
	fin = open(file)
	for line in fin:
		word = line.strip()
		if len(word)> 5:
			i = 0
			counter = 0
			while i < len(word)-1:
				letter1 = word[i]
				letter2 = word[i+1]
				if letter1 == letter2:
					counter += 1
					i += 1
					if counter >= 3:
						print word
				i += 1    
        
# print threeDoubles('words.txt')      


#-------------------------------------------------------------
#ex. 9.7

def threeConsecutiveDoubles(file):
	"""
	find a word that has 3 CONSECUTIVE double letters
	"""
	fin = open(file)
	for line in fin:
		word = line.strip()
		if len(word)> 5:
			i = 0
			j = 0
# 			counter = 0
			while i < len(word)-1:
				j = i
				if ((i + 1) < len(word)-1 ) and (word[i] == word[i+1]):
					#jump to next pair of letters
# 					print word, i, 'first loop'
					i += 2
					if ((i + 1) < len(word)-1 ) and (word[i] == word[i+1]):
						#jump to next pair
# 						print word, i, 'second loop'
						i += 2
						if ((i + 1) < len(word)-1 ) and (word[i] == word[i+1]):
							#print instead of return, to stay inside function
							print word
							break
				else:
					i = j + 1
				
     
# threeConsecutiveDoubles('words.txt')

#-------------------------------------------------------------
#ex. 9.8, initial & incorrect version...does not compute, since I'm disregarding all numbers below 100,000
#but DUH: 000001, 000002, 0020002, etc.
def odometerPalindromeXX():
	"""test all 6-digit numbers to find a three-sequence of palindromes: xx0000, x00000, 000000, all happening within three tick of the odometer."""
	#print all numbers with xx0000 palindrome
	i = 100000
	palindrome4 = []
	while i < 1000000:
		pTester = str(i)		
		if pTester[2::1] == pTester[:1:-1]:
			palindrome4.append(pTester)
		i += 1
	i = 0
	palindrome5 = []	
	while i < len(palindrome4):
		pTester = int(palindrome4[i])
		pTester += 1
		#then check to see which are x00000
		pTester = str(pTester)
		if pTester[1::1] == pTester[:0:-1]:
			palindrome5.append(pTester)
		i += 1
# 	print palindrome5
	i = 0
	palindrome6 = []
	while i < len(palindrome5):
		pTester = int(palindrome5[i])
		pTester += 1
		pTester = str(pTester)
		if pTester[::1] == pTester[::-1]:
			palindrome6.append(pTester)
		i += 1
	print palindrome6
		
	
# odometerPalindromeXX() 

#-------------------------------------------------------------
#ex. 9.8
#with help: using the pre-existing is_palindrome function 
# and learning about "%06d" for the leading zeros
#and don't need to store the results in a list--all the checking happens within each big loop

def is_palindrome(word):
    return word[::1] == word[::-1]

def odometerPalindrome():
	"""test all 6-digit numbers to find a three-sequence of palindromes: 
	xx0000, x00000, 000000, all happening within three tick of the odometer.
	"""
	#print all numbers with xx0000 palindrome
	mile = 0
	while mile < 1000000:
		mileStr = "%06d" % mile		
		if is_palindrome(mileStr[2::]):
			mile += 1
			mileStr = "%06d" % mile
			if is_palindrome(mileStr[1::]):
				mile += 1
				mileStr = "%06d" % mile
				if is_palindrome(mileStr):
					if len(mileStr) < 7:
						original = int(mileStr) - 2
						print mileStr, original
		else:
			mile += 1

# odometerPalindrome()


#-------------------------------------------------------------
#ex. 9.9.1
def is_palindrome2(word1, word2):
	return word1[::1] == word2[::-1]


def reverseAges(age1=0, age2=15):
	"""figure out an age based on: he and mom will have palindromic ages two more times. string method zfill suggested as useful
	assume leading zeros count? 02 == 20.
	assume max human age is 99? otherwise palindromes for bulk of reasonable ages are incorrect, or would need a decimal .0
	"""
	while age2 < 100:
		ageStr1 = "%02d" % age1
		ageStr2 = "%02d" % age2
		if is_palindrome2(ageStr1, ageStr2):
			print ageStr1, ageStr2
		age2 += 1
		age1 += 1
# 		print age1, age2

# reverseAges(0, 36)


#-------------------------------------------------------------
#ex. 9.9.2

def reverseAgesAll(ageDifference):
	"""figure out an age based on: he and mom will have palindromic ages two more times. string method zfill suggested as useful
	assume leading zeros count? 02 == 20.
	assume max human age is 99? otherwise palindromes for bulk of reasonable ages are incorrect, or would need a decimal .0
	"""
	age1 = 0
	age2 = ageDifference
	while age2 < 100:
		ageStr1 = "%02d" % age1
		ageStr2 = "%02d" % age2
		if is_palindrome2(ageStr1, ageStr2):
			print ageStr1, ageStr2
		age1 += 1
		age2 += 1
# 	ageDifference += 1
# 	print ageDifference

# reverseAgesAll(18)
# reverseAgesAll(25)

def ageRangeTester(startingRange):
	while startingRange < 60:
		print startingRange, ': ', reverseAgesAll(startingRange)
		startingRange += 1
	
ageRangeTester(12)


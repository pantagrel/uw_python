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
def uses_all(requiredLetters):
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
  
# print uses_all('aeiouy')

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
	abecedarian_words = 0
	fin = open(textFile)
	for line in fin:
		word = line.strip()	
		i = 0
		while i < len(word) - 1:
			if word[i + 1] >= word[i]:
# 				print word[i]
				i += 1
				if i == len(word) - 1:
					print word
					abecedarian_words += 1			
			else:
				break
	return abecedarian_words		
						
print abecedarianList('words.txt')

#-------------------------------------------------------------
#ex. 9.7 NOT FINISHED
# find a word that has 3 consequtive doubble letters
def threeDoubles(file):
  fin = open(file)
  for line in fin:
    word = line.strip()
    if len(word)> 5:
      i = 0
      while i < len(word)-1:
        counter = 0
        letter1 = word[i]
        letter2 = word[i+1]
        if letter1 == letter2:
          counter = counter + 1
          if counter == 3:
            print word
        i += 1    
     
        
        
#threeDoubles('words.txt')      


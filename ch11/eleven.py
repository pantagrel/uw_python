import random

#--------------------------------------------------------------------------------
"""
ex. 11.1
read words in 'words.txt' and store them as keys in a dictionary. values irrelevant.
then use 'in' to check whether string is stored in dictionary.
"""

def crosswordDictionary(file):
	fin = open(file)
	d = dict()
	for line in fin:
		word = line.strip()
		d[word] = len(word)
	return d 


def wordCheck(word, file):
	words = crosswordDictionary(file)
	if word in words:
		return True, word
	else:
		return False, word

#--------------------------------------------------------------------------------
"""
ex. 11.2
method: get() takes a key and a default value. if key is in dict, get() returns corresponding value. otherwise returns default value.
"""
def histogram(s):
	d = dict()
	for c in s:
		d[c] = d.get(c, 0) + 1
	return d 

#--------------------------------------------------------------------------------
"""
ex. 11.3
use keys() to return all the keys of a dictionary (returns as a list)
"""
def print_keys(file):
	d = crosswordDictionary(file)
	l = d.keys()
	l.sort()
	return l
	

#--------------------------------------------------------------------------------
"""
ex. 11.3 ALT
use keys() to return all the keys, values of a dictionary in alpha order
"""
def print_keysValuesAlt(file):
	d = crosswordDictionary(file)
	values = []
	for v in d:
		values.append(d[v])
	l = d.keys()
	newList = zip(l, values)
	newList.sort()
	return newList

#--------------------------------------------------------------------------------
"""
ex. 11.4
build and return a list of all keys that map to 'v'.
"""
def reverse_lookup(d, v):
	allKeys = []
	for k in d: 
		if d[k] == v:
			allKeys.append(k)
	return allKeys
	raise ValueError

#--------------------------------------------------------------------------------

if __name__ == "__main__":
	h = histogram('mary poppins')
	k = reverse_lookup(h, 3)
	print k	 

#	print print_keysValuesAlt('wordsA.txt')
#	print print_keys('words2.txt')
# 	print histogram('murphy is a goose seller, forsooth.')
# 	print wordCheck('sldkfjalds', 'words.txt')
# 	print wordCheck('snooze', 'words.txt')
# 	print crosswordDictionary('words2.txt')
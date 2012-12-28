import random

#--------------------------------------------------------------------------------
#ex. 11.1
"""
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


def wordCheck(word, d):
	words = d
	word = word.lower()
	if word in words:
		return True, word
	else:
		return False, word

# wordList = crosswordDictionary('words.txt')
# print wordCheck('AA', wordList)


#--------------------------------------------------------------------------------
#ex. 11.2
"""
method: get() takes a key and a default value. if key is in dict, get() returns corresponding value. otherwise returns default value.
"""
def histogram(s):
	d = dict()
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[c] += 1
	return d
	
# h = histogram('the moon is bright tonight upon the wabash.')
# print h

#--------------------------------------------------------------------------------
#ex. 11.2.2
"""
method: get() takes a key and a default value. if key is in dict, get() returns corresponding value. otherwise returns default value.
"""
def histogramSimple(s):
	d = dict()
	for c in s:
		d[c] = d.get(c, 0) + 1
	return d
	
histy = histogramSimple('the moon is bright tonight upon the wabash.')

# for k in h:
# 	print k, h[k]

#--------------------------------------------------------------------------------
# ex. 11.3
"""
use keys() to return all the keys and their values of a dictionary (returns as a list) in alpha order
"""
def print_hist(h):
	l = []
	for c in h:
		ltemp = [] #making nested lists of dict key/value pairs
		ltemp.append(c)
		ltemp.append(h[c])
		l.append(ltemp)
	l.sort()
	return l

# print print_hist(histy)
	

#--------------------------------------------------------------------------------
#ex. 11.3 ALT
"""
use keys() to return all the keys, values of a dictionary in alpha order
"""
def print_keysValuesAlt(d):
	values = []
	for v in d:
		values.append(d[v])
	l = d.keys()
	newList = zip(l, values)
	newList.sort()
	return newList

# print print_keysValuesAlt(histy)

#--------------------------------------------------------------------------------
#ex. 11.4
"""
build and return a list of all keys that map to value (v).
"""
def reverse_lookup(d, v):
	allKeys = []
	for k in d: 
		if d[k] == v:
			allKeys.append(k)
	return allKeys  #if this line is intented 2 levels, it returns just 1st key
	raise ValueError, "didn't work, tuffshitness."
	
# print reverse_lookup(histy, 2)

#--------------------------------------------------------------------------------
#ex. 11.5
"""
use 'setdefault' to write a concise version of invert_dict
"""
def invert_dict(d):
	inverse = dict()
	for k in d:
		v = d[k]
		if v not in inverse:
			inverse[v] = [k]
		else:
			inverse[v].append(k)
	return inverse

print invert_dict(histy)

def invert(d):
	
	d = d.setdefault(key, default=None) + 1


#--------------------------------------------------------------------------------
#ex. 11.6
"""

"""


#--------------------------------------------------------------------------------
#ex. 11.7
"""

"""





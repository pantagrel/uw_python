import urllib

'''
webStringy = urllib.urlopen('http://scintillus.com')
'''
#-------------------------------------------------------------
#ex. 9.1
#only print a word if it has more than 20 characters
def print_longWords(file):
    fin = open(file)
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print word

#print_longWords('words.txt')

#-------------------------------------------------------------
#ex. 9.2
#only print words with no 'e':

def has_no_e(file):
  fin = open(file)
  for line in fin:
    word = line.strip()
    if 'e' not in word:
      print word
      
#has_no_e('words.txt')      

#-------------------------------------------------------------
#ex. 9.2.2
#modify 9.2 to also compute percentage of words in list that have no 'e'

def has_no_ePercentage(file):
  counter_total = 0.0
  counter_no_e = 0.0
  fin = open(file)
  for line in fin:
    counter_total = counter_total + 1
    word = line.strip()
    if 'e' not in word:
      counter_no_e = counter_no_e + 1
  print (counter_no_e/counter_total) * 100, 'percent'

# has_no_ePercentage('words.txt')

#-------------------------------------------------------------
#ex. 9.3
# takes str + forbidden letters, returns True if letters aren't there

def avoids(word, str):
  checker_var = True 
  for char in str:
    if char in word:
      #print char
      checker_var = False
  return checker_var
    
#print avoids('i am flhying on a cloud of baro', 'llllltti')

#-------------------------------------------------------------
#ex. 9.3.2
# user inputs forbidden str, checks agains words.txt. prints ## of words that don't contain the forbidden str

def avoids_list():
  counter = 0
  counter_total = 0
  fin = open('words2.txt')
  str = raw_input('enter the forbidden letters:\n> ') 
  for line in fin:
    counter_total = counter_total + 1
    word = line.strip()
    for char in str:
      if char in word:
        print char
        print word
        counter = counter + 1    
#*********************************************************************
#once counter increments, move on to the next word. HOW TO DO!!!
#**********************
        print counter
  return counter_total - counter 
  
#print avoids_list()


#-------------------------------------------------------------
#ex. 9.4
# get word, str. return True is word uses only letters in str

def uses_only(string1, string2):
    tStr1 = list(string1)
    tStr2 = list(string2)
    tStr1.sort()
    tStr2.sort()
    if tStr1 == tStr2:
        return True
    else:
        return False

print 'ex. 9.4\n', uses_only('mooches', 'lite')


#-------------------------------------------------------------
#ex. 9.5
# word, str. build string using all letters in str at least once
def uses_all(word, str):
    for char in str:
        if char not in word:
            return False
    return True
  
#print uses_all('abucklp', 'abcp'), 'uses-all'



#-------------------------------------------------------------
#ex. 9.6
# 


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


if __name__ == "__main__":
	uses_only()
	    
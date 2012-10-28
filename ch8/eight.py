'''
fruit = 'banana'

index = 0
while index < len(fruit):
    letter = fruit[index]
    print letter
    index = index + 1

#do one that counts backwards, or spells the word out backwards


for char in fruit:
   print char

prefixes = 'JKLMNOPQ'
suffix = 'ack'
altSuffix = 'uack'

for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        print letter + altSuffix
    else:
        print letter + suffix

r = raw_input('enter a word at least 5 letters long\n> ')

print r[0:4]
print "'" + r[4:] + "' is the rest of the string"


s = "monty python"
#this prints the whole string--seems to default to 0, length -1

print s[:]


#strings are immutable, but can be variables resassigned
hi = 'hello'
newHi = 'J' + hi[1:]
print hi
print newHi

'''

#searching
def find(word, letter, start):
    #set index to 0
    index = start
    #start a loop that is as long as the string put into function
    while index < len(word):
        #check if letter at position [index] == the letter input into function
        if word[index] == letter:
            #if it matches, return that index int value 
            return index
        #if it doesn't match yet, increment index and repeat the loop    
        index = index + 1
    #if no match is found, return -1
    return -1

#s = find('yellow', 'w', 3)
#print s

def letterCounter(word, whichLetter):
    count = 0
    for letter in word:
        if letter == whichLetter:
            count = count + 1
    print count

letterCounter('respecting', 'g')
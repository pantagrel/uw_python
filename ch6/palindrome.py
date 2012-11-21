def first(word):
    return word[0]

def middle(word):
    return word[1:-1]
    
def last(word):
    return word[-1]
    

# print first('first')
# print middle('sherry')
# print last('house')



def is_palindrome(word):
    """word is type str. checks if a word is a palindrome."""
    if first(word) != last(word):
        print 'not a palindrome'
        return False
    else:
        return is_palindrome(middle(word))
        
is_palindrome('kayak')
 

"""
implement the function isWordGuessed that takes in two 
parameters - a string, secretWord, and a list of letters, lettersGuessed. This 
function returns a boolean - True if secretWord has been guessed (ie, all the 
letters of secretWord are in lettersGuessed) and False otherwise.
"""
def isWordGuessed(secretWord, lettersGuessed):
    
    
    for x in secretWord:
        if x not in lettersGuessed:
            return False
    return True

secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(isWordGuessed(secretWord, lettersGuessed))

"""
Next, implement the function getGuessedWord that takes in two parameters - a 
string, secretWord, and a list of letters, lettersGuessed. This function 
returns a string that is comprised of letters and underscores, based on what
letters in lettersGuessed are in secretWord. This shouldn't be too different 
from isWordGuessed!
"""
def getGuessedWord(secretWord, lettersGuessed):
    
    my_String = ''
    for x in secretWord:
        if x in lettersGuessed:
            my_String += x
        else:
            my_String += '_'
    return my_String
#testcase
secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getGuessedWord(secretWord, lettersGuessed))

"""
Next, implement the function getAvailableLetters that takes in one parameter - 
a list of letters, lettersGuessed. This function returns a string that is 
comprised of lowercase English letters - all lowercase English letters that 
are not in lettersGuessed.
"""

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    notGuessed = ''
    for x in 'abcdefghijklmnopqrstuvwxyz':
        if x not in lettersGuessed:
            notGuessed += x
    return notGuessed

#testcase
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))



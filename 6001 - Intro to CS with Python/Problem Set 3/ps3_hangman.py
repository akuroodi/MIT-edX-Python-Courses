# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

# Edit path to 'words.txt' file as needed
WORDLIST_FILENAME = "/Users/adityakuroodi/Documents/PythonClass/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
   
    y = [False for x in set(secretWord) if x not in lettersGuessed]
    return all(y)

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    return "".join(x if x in lettersGuessed else ' _ ' for x in list(secretWord) )

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed. In alphabetical order.
    '''
    import string
    x = string.ascii_lowercase

    y = "".join(z for z in list(x) if z not in lettersGuessed)
    return y

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    print("-------------")

    numGuesses = 8          # every game starts with 8 guesses
    lettersGuessed = []     # empty list to initialize which letters have been guessed

    while(numGuesses > 0):
      
      if(isWordGuessed(secretWord, lettersGuessed)):
        print("Congratulations, you won!")
        break
      
      print("You have " + str(numGuesses) + " guesses left.")

      print("Available letters: " + getAvailableLetters(lettersGuessed))

      x = input("Please guess a letter: ")
      
      if (x in lettersGuessed):
        print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        print("-------------")
        continue   
      else:
        lettersGuessed.append(x)
      
      if (x in secretWord):
        print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
        print("-------------")
        continue

      else:
        print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
        print("-------------")
        numGuesses -= 1
      
    if (numGuesses == 0):
      print("Sorry, you ran out of guesses. The word was " + secretWord + ".")



secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

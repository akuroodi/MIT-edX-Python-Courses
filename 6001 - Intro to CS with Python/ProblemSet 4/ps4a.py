# The 6.00 Word Game

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 
    'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 
    'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

# Edit path of this constant to wherever you download the 'words.txt' file
WORDLIST_FILENAME = "/Users/adityakuroodi/Documents/PythonClass/Problem Sets/ProblemSet4/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------


def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # TO DO ... <-- Remove this comment when you code this function
    score = 0

    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter]
    
    score *= len(word)

    if len(word) == n: score += 50

    return score


def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line


def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function

    hand2 = hand.copy()

    for letter in word:
        hand2[letter] -= 1

    for letter in set(word):
        if(hand2[letter] == 0): hand2.pop(letter)

    return hand2


def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function

    if (word not in wordList): return False

    x = []
    for letter in hand.keys():                  # makes a list of hand capturing frequency of letters
       for j in range(hand[letter]):
           x += letter
           
    for letter in word:                         # for each letter check that it's in the hand
       if (letter not in hand.keys()): return False
       
       elif (letter not in x): return False     # also check that there is enough of that letter still in hand
       
       else: x.remove(letter)           # for each used letter, remove it from list and continue
            
    return True

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function

    x = "".join(key*value for (key,value) in hand.items() )

    return len(x)

    # alternatively
    # return sum (hand.values())



def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    score = 0
    # Keep track of the total score
    
    # As long as there are still letters left in the hand:
    while (calculateHandlen(hand) > 0):
        
        # Display the hand
        print("Current Hand: ", end = "")
        displayHand(hand)
        
        # Ask user for input
        Input = input('Enter word, or a "." to indicate that you are finished: ')
        
        # If the input is a single period:
        if (Input == "."): break
            # End the game (break out of the loop)

            
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if (isValidWord(Input, hand, wordList) != True):

                # Reject invalid word (print a message followed by a blank line)
                print("Invalid word, please try again." + "\n")
                continue


            # Otherwise (the word is valid):
            elif (isValidWord(Input, hand, wordList)):
                # Tell the user how many points the word earned,
                #  and the updated total score, in one line followed by a blank line

                points = getWordScore(Input, n)
                score += points

                print( '"{}"'.format(Input) + " earned " + str(points) + " points.", end = " ")
                print("Total: " + str(score) + " points. \n")
                
                # Update the hand 
                hand = updateHand(hand, Input)

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if (calculateHandlen(hand) == 0):
        print("Run out of letters. Total score: " + str(score) + " points.")
    
    else:
        print("Goodbye! Total score: " + str(score) + " points.")

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    firstTime = True
   
    while (True):
        
        x = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")

        if (x == 'n'):
            hand = dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE)
            firstTime = False

        
        elif (x == 'r' and firstTime):
            print("You have not played a hand yet. Please play a new hand first!\n")
            continue

        elif (x == 'r' and firstTime == False):
            playHand(hand, wordList, HAND_SIZE)
            continue

        elif (x == 'e'):
            break
        
        else:
            print("Invalid command.")
            continue




#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)



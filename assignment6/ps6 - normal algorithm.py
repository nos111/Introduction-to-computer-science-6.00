# 6.00 Problem Set 6
#
# The 6.00 Word Game
#

import random
import string
import time
from itertools import permutations

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

    
def get_frequency_dict(sequence):
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

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all n letters are used on
    the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    score = 0
    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter.lower()]
    if len(word) == n:
        score += 50
    return score
#build a new dictionarry with the sorted words as keys and the original word as value
#takes the words list as parameter and return a new rearanged list
def get_word_rearrangements(words_list):
    #for every word:
    #rearrange it's letters alphabetically
    #build a key with the rearranged word
    #make the value of the key the real word
    rearranged_list = {}
    for word in words_list:
        rearranged_list[''.join(sorted(word))] = word
    return rearranged_list
    

#change the words list to a dicationary where every word is mapped to its value
#this way we can access the word and it's value instantly
#the function takes a list and return a dictionary with the words value
#the word is the key and the value is the points you get for it
def get_words_to_points(words_list):
    points_dic = {}
    for word in words_list:
        score = get_word_score(word,0)
        points_dic[word] = score
    return points_dic

#build a word out of the hand
#check if it's valid
#find the best combination of words
def pick_best_word(hand,points_dic):
    work_hand = []
    for letter in hand.keys():
        for j in range(hand[letter]):
             work_hand.append(letter)
    print work_hand
    #split the hand into a list
    hand = list(hand)
    #make all possible words from a hand
    possible_words = list(''.join(letters) for letters in permutations(hand))
    print len(possible_words)
    #try all words with full hand
    for word in possible_words:
        value = is_valid_word(word,points_dic)
        if value > 0:
            print word,value
            return word
    #split the list into two
    hand_one = hand[:4]
    hand_two = hand[4:]
    #make all possible words from the split
    possible_word_one = list(''.join(letters) for letters in permutations(hand_one))
    possible_word_two = list(''.join(letters) for letters in permutations(hand_two))
    #test them
    for word in possible_word_one:
        value = is_valid_word(word,points_dic)
        if value > 0:
            print word,value
            return word
    for word in possible_word_two:
        value = is_valid_word(word,points_dic)
        if value > 0:
            print word,value
            return word
    print 'No solution found'
    
        
    


#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                              # print an empty line

#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
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
    num_vowels = n / 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    freq = get_frequency_dict(word)
    newhand = {}
    for char in hand:
        newhand[char] = hand[char]-freq.get(char,0)
    return newhand
    #return dict( ( c, hand[c] - freq.get(c,0) ) for c in hand )
        

#
# Problem #3: Test word validity
#
def is_valid_word(word, points_dic):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    value = points_dic.get(word,0)
    return value

#
# Problem #4: Playing a hand
#
def play_hand(hand, points_dic):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """    
    original_limit_time = input('Enter time limit, in seconds, for players: ')
    time_limit = original_limit_time
    print 'Current Hand:',
    display_hand(hand)
    start_time = time.time()
    pick_best_word(hand, points_dic)
    end_time = time.time()
    total_time = end_time - start_time 
    total_time = round(total_time)
    if total_time == 0:
        total_time = 1
    print 'Time used to calculate answer %s seconds' %total_time


#
# Problem #5: Playing a game
# Make sure you understand how this code works!
# 
def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """

    hand = deal_hand(HAND_SIZE) # random init
    cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
    if cmd == 'n':
        hand = deal_hand(HAND_SIZE)
        play_hand(hand.copy(), word_list)
        print
    elif cmd == 'r':
        play_hand(hand.copy(), word_list)
        print
    elif cmd == 'e':
        return
    else:
        print "Invalid command."

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    rearranged_list = get_word_rearrangements(word_list)
    print rearranged_list['aaghhrr']
    points_dic = get_words_to_points(word_list)
    play_game(points_dic)

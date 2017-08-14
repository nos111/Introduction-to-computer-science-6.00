# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 21:44:33 2017

@author: Dell
"""

import random

import re

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

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

# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

# TO DO: your code begins here!

#define global variables which are the active player and the fragment as empty fragment
active_player = 'Player one'
fragment = ''

#this is the main function in the game.
#It shows how the control will flow in the game and what steps will be taken
#it takes the acitve player, the empty fragment and the words list as parameters
def ghost(active,frag,list_words):
    #initiate end game variable with false value when we begin
    end_game = False
    #text to be displayed showing the players turn
    text = active + ' may enter a letter: '
    #catch the user input
    letter = raw_input(text)
    #check if the input is valid
    letter = check_letter(letter)
    #add the new input to the fragment
    fragment = add_letter(frag,letter)
    #if we have a false value from the user we will stop the control here and return to the begining
    if letter == False:
        print 'Please enter a valid letter'
        return ghost(active,frag,list_words)
    #if the fragment length is 4 than it's time to check what words does it match
    if len(fragment) > 3:
        #use regexp to check the matching items
        list_words = find_match(fragment,list_words)
        #check if we have a winner or loser to see if it's time to end the game
        end_game = check_winner(active,fragment,list_words)
    #if we don't have a winner the game will continue
    if end_game == False:
        #change the player turn
        active = change_player(active)
        print fragment
    else:
        #if the end game is true, than end this function and return
        return
    #if we haven't ended the game than it's time for another turn
    return ghost(active,fragment,list_words)
        

    

#function to switch player
#takes the current player and switch to the other player
#return the new player name
def change_player(player):
    if player == 'Player one':
        player = 'Player two'
        return player
    else:
        player = 'Player one'
        return player
        
#check if the letter input we asked for is valid  
#takes the letter as parameter, returns the letter if it's valid or false if it's not  
def check_letter(letter):
    #if the player enters more than one letter return the rejection
    if len(letter) > 1:
        return False
    #if the player doesn't enter anything reject his input
    if letter == '':
        return False
    #if the letter exists, turns it into lower case and return the letter
    #our list is in lower case. If we don't change to lower case we won't have matches
    if letter in string.ascii_letters:
        letter = letter.lower()
        return letter
    #if the letter doesn't exist, reject the entry
    elif letter not in string.ascii_letters:
        return False

#check if one of the players has won the game
#takes the current player, the current fragment and the words list as parameters
#checks if we have a perfect match in the words 
def check_winner(player,frag,words_list):
    #first check that we still have items in the list
    if len(words_list) == 0 :
        print player, ' has lost'
        return True
    #if we have items, loop over to check if we have a full match
    for word in words_list:
        if frag == word:
            print player, ' has won'
            return True
    #if nothing qualifies return false for the game to continue
    return False
    
#use regex to minimize the search list
#this why we make our search much faster everytime and limit our possibilities
#takes the regexp and the list as parameters
#returns a new list with the matching items
def find_match(reg,list):
    #initiate an empty list to return
    matches_list = []
    #loop over the regexp matches and append them to the list
    for fragment in list:
        if re.search('^' + reg, fragment):
            matches_list.append(fragment)
    return matches_list      
            
#add a letter to the fragment
#takes a letter and the fragment as parameters
#returns the new fragment 
def add_letter(fragment,letter):
    #first check that the letter is a string
    if type(letter) == str:
        text = fragment + letter
        return text
    #if not a string return the fragment without adding it
    else:
        return fragment


if __name__ == '__main__':
    ghost(active_player, fragment,wordlist)










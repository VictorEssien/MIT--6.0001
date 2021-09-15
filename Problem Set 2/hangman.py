# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 14:27:39 2021

@author: Victor
"""

# Problem Set 2, hangman.py
# Name: Victor
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words-Copy1.txt"

def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
    
word_list = load_words()




def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing; Assumes all letters are 
        lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
        Assumes all letters are lowercase
    returns: boolean, True if all the letters of the secret_word are in letters_guessed;
        False otherwise
    """
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True




def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    
    letters_guessed: list (of letters), which letters have been guessed so far
    
    returns: string, comprised of letters, underscores (_), and spaces that represents
        which letters in secret_word have been guessed so far.
        
    """    
    guessed_word = ""
          
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += "_ "
        return guessed_word   
            


            
def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
        yet been guessed.
        
    """  
    lowercase_letters = string.ascii_lowercase   #Returns all lowercase letters in the English alphabet
    
    available_letters = ""
    same_letters = ""
    
    for i in lowercase_letters:
        if i in letters_guessed:
            same_letters += i
        else:
            available_letters += i
            
    return available_letters




def hangman(secret_word):
    """
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    
    """
    secret_words = str(secret_word.lower())
    vowels = "aeiou"
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letters long".format(len(secret_words)))
    
    guesses_remaining = 6
    warnings_remaining = 3
    counter = 0
    letters = []  #To keep track of the right guesses
    guesses = []  #To keep track of all the user's guesses
    
    print("You have {} warnings left.".format(warnings_remaining))
    print("-------------")
    
    while guesses_remaining > counter:
        available_letters = get_available_letters(guesses)
        print("You have {} guesses left.".format(guesses_remaining))
        print("Available letters: {}".format(available_letters))
        
        #print("Available letters: {}".format(get_available_letters(guesses)))
        
        letter_guessed = str(input("Please guess a letter: "))
        letter_guessed.lower()
    
        guesses += letter_guessed
        word = get_guessed_word(secret_words, letters)
        
        if letter_guessed.isalpha() == False:  #To check if the letter guessed is an alphabet
            if warnings_remaining >= 1:
                warnings_remaining -= 1
                print("Oops! That is not a valid letter.",
                      "You have {} warnings left: {}".format(warnings_remaining, word))
            
            else:
                print("Oops! That is not a valid letter.",
                      "You have no warnings left so you lose a guess")
                guesses_remaining -= 1
                
        if letter_guessed.isalpha() == True:
            if letter_guessed in secret_words and letter_guessed in available_letters:
                letters += letter_guessed
                correct_word = get_guessed_word(secret_words,letters)
                print("Good guess:", correct_word)
                    
            elif letter_guessed not in available_letters and warnings_remaining >= 1:
                warnings_remaining -= 1
                print("Oops! You have already guessed that letter.",
                      "You now have {} warnings left: {}".format(warnings_remaining, word))
            
            elif letter_guessed not in available_letters and warnings_remaining < 1:
                guesses_remaining -= 1
                print("Oops! You have already guessed that letter. You now have no warnings left",
                      "so you lose a guess: {}".format(word))
            
            elif letter_guessed not in secret_words:
                if letter_guessed in vowels:
                    guesses_remaining -= 2
                    print("Oops! That letter is not in my word:", word)
                    
                else:
                    guesses_remaining -= 1
                    print("Oops! That letter is not in my word:", word)
            
        print("-------------")
        
        if guesses_remaining <= counter:
            return ("Sorry, you ran out of guesses. The word was {}".format(secret_word))
        
        else:
            if is_word_guessed(secret_word, letters) == True:
                print("Congratulations, you won!")
                
                unique_letters = []
                
                for letter in secret_word:
                    unique_letters += letter
                    
                return ("Your total score is:", guesses_remaining * len(unique_letters))
            
            

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------




def match_with_gaps(my_word, other_word):
    """
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
        
    """
    current_guess = ""
    
    
    for char in my_word:
        if char != " " :
            current_guess += char
    #print(current_guess)  
    
    if len(current_guess) != len(other_word):
        return False
        
    for i in range(len(other_word)):
        if current_guess[i] != "_" and current_guess[i] != other_word[i]:
            return False
        if current_guess[i] == "_" and other_word[i] in current_guess:
            return False
    return True





def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible_matches = ""
    
    for word in word_list:
        if match_with_gaps(my_word, word) == True:
            possible_matches += word + " "
    
    if len(possible_matches) == 0:
        return ("No matches found")
    else:
        print("Possible matches:")
        return possible_matches
    
    


def hangman_with_hints(secret_word):
    """
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    
    """
    secret_words = str(secret_word.lower())
    #word_list = load_words()
    #complete_letters = string.ascii_lowercase
    vowels = "aeiou"
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letters long".format(len(secret_words)))
    
    guesses_remaining = 6
    warnings_remaining = 3
    counter = 0
    letters = []  #To keep track of the right guesses
    guesses = []  #To keep track of all the user's guesses
    
    print("You have {} warnings left.".format(warnings_remaining))
    print("-------------")
    
    while guesses_remaining > counter:
        available_letters = get_available_letters(guesses)
        print("You have {} guesses left.".format(guesses_remaining))
        print("Available letters: {}".format(available_letters))
        
        letter_guessed = str(input("Please guess a letter: "))
        letter_guessed.lower()
    
        guesses += letter_guessed
        word = get_guessed_word(secret_words, letters)
        
        if letter_guessed.isalpha() == False:  #To check if the letter guessed is an alphabet
            if letter_guessed == "*":
                user_guess = get_guessed_word(secret_word, letter_guessed)
                print(show_possible_matches(user_guess))
                
            elif warnings_remaining >= 1:
                warnings_remaining -= 1
                print("Oops! That is not a valid letter.",
                      "You have {} warnings left: {}".format(warnings_remaining, word))
            
            else:
                print("Oops! That is not a valid letter.",
                      "You have no warnings left so you lose a guess")
                guesses_remaining -= 1
                
        if letter_guessed.isalpha() == True:
            if letter_guessed in secret_words and letter_guessed in available_letters:
                letters += letter_guessed
                correct_word = get_guessed_word(secret_words,letters)
                print("Good guess:", correct_word)
                    
            elif letter_guessed not in available_letters and warnings_remaining >= 1:
                warnings_remaining -= 1
                print("Oops! You have already guessed that letter.",
                      "You now have {} warnings left: {}".format(warnings_remaining, word))
            
            elif letter_guessed not in available_letters and warnings_remaining < 1:
                guesses_remaining -= 1
                print("Oops! You have already guessed that letter. You now have no warnings left",
                      "so you lose a guess: {}".format(word))
            
            elif letter_guessed not in secret_words:
                if letter_guessed in vowels:
                    guesses_remaining -= 2
                    print("Oops! That letter is not in my word:", word)
                    
                else:
                    guesses_remaining -= 1
                    print("Oops! That letter is not in my word:", word)
            
        print("-------------")
        
        if guesses_remaining <= counter:
            return ("Sorry, you ran out of guesses. The word was {}".format(secret_word))
        
        else:
            if is_word_guessed(secret_word, letters) == True:
                print("Congratulations, you won!")
                
                unique_letters = []
                
                for letter in secret_word:
                    unique_letters += letter
                    
                return ("Your total score is:", guesses_remaining * len(unique_letters))
            
            
            
# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)
    #secret_word = 'else'
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(word_list)
    hangman_with_hints(secret_word)

#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Ryan Prance & Paramvir Singh'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def pig_latinify(word):
    """
    Take in word and returns pig latin translation of word
    :param :
    word -> str
    :return:
    pig latin translation of that word
    :raises:
    ERROR if word is not alphanumeric
    ERROR if word is not a str

    """
    #check to make sure that word is both string and contains letter characters
    if type(word) is str and word.isalpha():
        suffix1 = "yay"
        suffix2 = "ay"
        #define step variable to loop through letter positions
        step = 0
        #make the word all lower case
        word = word.lower()
        #define vowels as list
        vowels = list("aeiouy")
        #define first letter

        #begin looping through the letters
        for letter in word:
            first_letter = word[0]
            #if the first letter is a vowel, stop and return word plus yay
            if first_letter in vowels:
                return word + suffix1
            #if the last condition is not satisfied
            #go through the letters at step value
            elif word[step] in vowels:
                #if the letter in that position is in the list
                #slice the word from step then add sliced word up to step plus the second suffix
                return word[step:] + word[:step] + suffix2
            #if the letter at position is not in vowels, add 1 to step and check again
            step += 1
    else:
        return("ERROR")




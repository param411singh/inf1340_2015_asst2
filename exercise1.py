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
    Describe your function


    :param : any word
    :return: pig latin translation of that word
    :raises:

    """
   #create step value
    a = 0

    x = "yay"
    y = "ay"
    #define vowels as list
    vowels = list("aeiouy")
    first_letter = word[a]
    for letter in word:
        #if the word starts with a vowel, give the word plus suffix x
        if first_letter in vowels:
            return word + x
        #if the previous condition is false
        elif word[a] in vowels:
            #move through letter positions until vowel is found
            #when vowel found, slice from a to end of word, add a, and add y
            return word[a:] + word[:a] + y

        a += 1



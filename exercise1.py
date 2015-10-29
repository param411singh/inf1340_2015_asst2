#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def pig_latinify(word):
    """
    Describe your function


    :param :
    :return:
    :raises:

    """
    a = 0
    for index in word:
        first_letter = word[a]
        if first_letter in ('a', 'e', 'i', 'o', 'u'):
            return word[a:] + "yay"
        else:
            a += 1
            letter = word[a]
            if letter in ('a', 'e', 'i', 'o', 'u'):
                return word[a:] + word[:a] + "ay"


print pig_latinify(word="apple")

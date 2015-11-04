#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

This module converts performs substring matching for DNA sequencing

"""

__author__ = 'Ryan Prance & Paramvir Singh'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def find(input_string, substring, start, end):
    """
    Describe your function

    :param :
    :return:
    :raises:

    """

    sublen = (len(substring))

    for i in range(start, end):
        if input_string[i:(i+sublen)] == substring:
            return i
        else:
            i += 1
    return -1


def multi_find(input_string, substring, start, end):
    """
    Describe your function

    :param :
    :return:
    :raises:

    """
    loop = True
    #define an empty string
    nulist = ""
    #send start value back one so end value is what it would be if starting from 0
    r = start - 1
    while loop:
        r = find(input_string, substring, r + 1, end)
        if r != -1:
            if nulist == "":
                nulist += str(r)
            else:
                nulist += "," + str(r)
        else:
            loop = False
    return nulist

print multi_find("Ni! Ni! Ni! Ni!", "dog", 0, 20)


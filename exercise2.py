#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

This module converts performs substring matching for DNA sequencing

"""

__author__ = 'Susan Sim'
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
    i = 0
    x = (len(substring))

    for i in range(0, len(input_string)):
        if input_string[i:(i+x)] == substring:
            print i
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
    j = 0
    x = (len(substring))

    while j <= len(input_string):
        for i in range(0, len(input_string)):
            if input_string[i:(i+x)] == substring:
                print i
            else:
                i += 1
                j += len(input_string)
    result = ""

    return result

find("This is an ex-parrot", "an", 0, 20)
multi_find("Ni!sk Ni!sk Ni!sk Ni!sk", "sk", 0, 20)
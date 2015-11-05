#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

Test module for exercise2.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from exercise2 import find, multi_find


def test_find_basic():
    """
    Test find function.
    """
    assert find("This is an ex-parrot", "parrot", 0, 20) == 14

    # Test using integers
    assert find(411926345, 11, 0, 9) == 1

    # Test using special characters
    assert find("!@#$ $#@& %$#@ ^%$#", "^", 0, 19) == 15


def test_multi_find_basic():
    """
    Test multi_find function.
    """
    assert multi_find("Ni! Ni! Ni! Ni!", "Ni", 0, 20) == "0,4,8,12"


def test_find_nothing():
    assert find("Ni! Ni! Ni! Ni!", "Hi", 0, 20) == "No Match Found"


def test_multi_find_nothing():
    assert multi_find("Ni! Ni! Ni! Ni!", "Hi", 0, 20) == "No Match Found"

    # Test using integers
    multi_find(4112341156411, 411, 0, 13) == "0,5,10"

    # Test using special characters
    multi_find("!@#$ $#@! ^%$! !@*(", "!", 0, 18) == "0,8,13,15"

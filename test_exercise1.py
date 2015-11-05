#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

Test module for exercise1.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


from exercise1 import pig_latinify


def test_basic():
    """
    Basic test cases from assignment hand out
    """
    assert pig_latinify("dog") == "ogday"
    assert pig_latinify("scratch") == "atchscray"
    assert pig_latinify("is") == "isyay"
    assert pig_latinify("apple") == "appleyay"
    assert pig_latinify("python") == "ythonpay"
    assert pig_latinify("APPLE") == "appleyay"

    # when a word containing multiple vowels is passed in as a parameter
    assert pig_latinify("paramvir") == "aramvirpay"


def test_illegal():
    """
    checks that program returns ERROR if illegal input is encountered

    """

    # when an integer is passed in as a parameter
    assert pig_latinify(123) == "ERROR"

    # when a string containing numbers is passed in as a parameter
    assert pig_latinify("123") == "ERROR"

    # when special characters are provided
    assert pig_latinify("!@#$%") == "ERROR"

    # when alphanumeric string is passed in as a parameter
    assert pig_latinify("as123f") == "ERROR"

    # when an empty string is passed in as a parameter
    assert pig_latinify("") == "ERROR"




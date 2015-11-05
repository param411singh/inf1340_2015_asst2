#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

Test module for exercise3.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from exercise3 import union, intersection, difference, MismatchedAttributesException


###########
# TABLES ##
###########
GRADUATES = [["Number", "Surname", "Age"],
             [7274, "Robinson", 37],
             [7432, "O'Malley", 39],
             [9824, "Darkes", 38]]

MANAGERS = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]

STUDENTS = [["Name", "Student No", "Program", "Course"],
            ["Ryan", 1002178216, "ISD", 1341],
            ["Param", 1002178213, "KMD", 1340],
            ["Mibin", 1002176123, "KMIM", 2176],
            ["Steph", 1002154321, "LIS", 8712]]

COURSES = [["Name", "Student No", "Program", "Course"],
           ["Ryan", 1002178216, "ISD", 1341],
           ["Michael", 100218765, "LIS", 1234],
           ["Param", 1002178213, "KMD", 1340],
           ["John", 1002123442, "CRO", 1276]]

FACULTY = [["Name", "Employee ID", "Program", "Course"],
           ["Eric", 8716234, "ISD", 1341],
           ["Susan", 8716243, "KMD", 1340],
           ["Colin", 9876541, "LIS", 1234],
           ["Nina", 7561342, "ARM", 5465],
           ["Tom", 1312343, "CRO", 4325]]


#####################
# HELPER FUNCTIONS ##
#####################
def is_equal(t1, t2):
    return set(map(tuple, t1)) == set(map(tuple, t2))


###################
# TEST FUNCTIONS ##
###################
def test_union():
    """
    Test union operation.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37],
              [9297, "O'Malley", 56],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    result_2 = [["Name", "Student No", "Program", "Course"],
                ["Ryan", 1002178216, "ISD", 1341],
                ["Param", 1002178213, "KMD", 1340],
                ["Michael", 100218765, "LIS", 1234],
                ["Mibin", 1002176123, "KMIM", 2176],
                ["Steph", 1002154321, "LIS", 8712],
                ["John", 1002123442, "CRO", 1276]]

    assert is_equal(result, union(GRADUATES, MANAGERS))
    assert is_equal(result_2, union(STUDENTS, COURSES))

    # Test Case when the Schemas don't match
    try:
        assert union(GRADUATES, STUDENTS)
    except MismatchedAttributesException:
        pass


def test_intersection():
    """
    Test intersection operation.
    """
    result = [["Number", "Surname", "Age"],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    result_2 = [['Name', 'Student No', 'Program', 'Course'],
                ['Ryan', 1002178216, 'ISD', 1341],
                ['Param', 1002178213, 'KMD', 1340]]

    assert is_equal(result, intersection(GRADUATES, MANAGERS))
    assert is_equal(result_2, intersection(STUDENTS, COURSES))


def test_difference():
    """
    Test difference operation.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37]]

    result_2 = [["Name", "Student No", "Program", "Course"],
                ["Mibin", 1002176123, "KMIM", 2176],
                ["Steph", 1002154321, "LIS", 8712]]

    assert is_equal(result, difference(GRADUATES, MANAGERS))
    assert is_equal(result_2, difference(STUDENTS, COURSES))

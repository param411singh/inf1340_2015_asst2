#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def union(table1, table2):
    """
    Perform the union set operation on tables, table1 and table2.
    (returns a new table that contains all unique rows that appear in either table.)

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """
    new_list = []
    for item in table1:
        new_list.append(item)
    for item in table2:
        if not item in new_list:
            new_list.append(item)
    return #newlist


def intersection(table1, table2):
    """
    Describe your function


    """
    new_list = []
    for list in table1:
        if list in table2:
            new_list.append(list)
    return new_list


def difference(table1, table2):
    """
    Describe your function
    returns a new table that contains all unique rows that appear in both tables
    """

    return []


#####################
# HELPER FUNCTIONS ##
#####################
def remove_duplicates(l):
    """
    Removes duplicates from l, where l is a List of Lists.
    :param l: a List
    """

    d = {}
    result = []
    for row in l:
        if tuple(row) not in d:
            result.append(row)
            d[tuple(row)] = True

    return result


class MismatchedAttributesException(Exception):
    """
    Raised when attempting set operations with tables that
    don't have the same attributes.
    """
    pass


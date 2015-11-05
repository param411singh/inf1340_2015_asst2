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
    (returns a new table that contains all unique rows that appear
    in either table.)

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """

    # Initiate by testing whether the schemas of the two tables match or not
    if table1[0] == table2[0]:
        # If the schemas match, assign the schema to a new table
        table3 = [table1[0]]
        if len(table1) >= len(table2):
            for i in range(1, len(table1)):
                if table1[i] not in table3:
                    table3 += [table1[i]]
                    for j in range(1, len(table2)):
                        if table2[i] not in table3:
                            table3 += [table2[i]]
        else:
            for i in range(1, len(table2)):
                if table2[i] not in table3:
                    table3 += [table2[i]]
                    for j in range(1, len(table1)):
                        if table1[j] not in table3:
                            table3 += [table1[j]]
    else:
        raise MismatchedAttributesException
    return table3


def intersection(table1, table2):
    """
    Performs the intersection set of operations on the tables:
    table1 and table2
    If the two tables have similar schema and some common rows,
    it returns the schema as well as the common rows
    Otherwise it raises the MismatchedAttributesException
    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """

    # Check whether the schemas of the two tables match
    if table1[0] == table2[0]:
        # If the schemas match, assign the schema to a new table
        table3 = [table1[0]]
        for i in range(1, len(table1)):
            for j in range(1, len(table2)):
                if table1[i] == table2[j]:
                    table3 += [table1[i]]
    else:
        raise MismatchedAttributesException
    return table3


def difference(table1, table2):
    """
    Performs the difference set of operations on the tables: table1 and table2
    If the two tables have similar schema and some uncommon rows,
    it returns the schema as well as the uncommon rows
    Otherwise it raises the MismatchedAttributesException
    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """

    # Check whether the schemas of the two tables match
    if table1[0] == table2[0]:
        # If the schemas match, assign the schema to a new table
        table3 = [table1[0]]
        for i in range(1, len(table1)):
                if table1[i] not in table2:
                    table3 += [table1[i]]
    else:
        raise MismatchedAttributesException
    return table3


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


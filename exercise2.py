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

    The function provides the start index of the substring in a larger input string

    :param : a string passed as an argument from the test cases or from the other function
    :return: the start index of the substring if the substring is found, else returns "No Match Found"

    """

    # Convert any integer or special character to a string
    input_string = str(input_string)
    substring = str(substring)
    length_of_substring = (len(substring))
    for index in range(start, end):
        if input_string[index: (index + length_of_substring)] == substring:
            return index
        else:
            index += 1
    return "No Match Found"


def multi_find(input_string, substring, start, end):
    """

    The function provides multiple indices related to the instances of substring in the larger string

    :param : a string passed as an argument from the test cases
    :return: the start indices of the substring if the substring is found, else returns "No Match Found"

    """
    # convert arguments into string if not passed as strings
    input_string = str(input_string)
    substring = str(substring)

    # define an empty string
    list_for_storing_index = ""

    # send start value back one so end value is what it would be if starting from 0
    result = start - 1

    loop = True
    while loop:
        result = find(input_string, substring, result + 1, end)
        if result != "No Match Found":
            if list_for_storing_index == "":
                list_for_storing_index += str(result)
            else:
                list_for_storing_index += "," + str(result)
        else:
            loop = False

    # check whether any match for the substring is found or not
    if list_for_storing_index == "":
        return "No Match Found"
    else:
        return list_for_storing_index


"""
    loop = True
    index = start - 1
    new_list = ""
    while loop is True:
        result = find(input_string, substring, index + 1, end)
        if result != "No Match Found":
            if new_list is None:
                new_list += str(result)
            else:
                new_list += "," + str(result)
        else:
            loop = False
    print("hello")
    if new_list is None:
        return "No Match Found"
    else:
        return new_list
"""

"""
    Exercise done without using the find function

    # Convert any integer or special character to a string
    input_string = str(input_string)
    substring = str(substring)
    list_for_storing_index = []
    # Define and initialise a counter for comparing individual letters
    counter = 0
    substring_length = (len(substring))
    while counter <= len(input_string):
        for index in range(start, end):
            if input_string[index:(index + substring_length)] == substring:
                list_for_storing_index.append(index)
            else:
                index += 1
                counter += len(input_string)
    # Take out individual index values from the list_for storing_index and return them as a string
    if list_for_storing_index is None:
        return "No Match Found"
    else:
        return ",".join([str(z) for z in list_for_storing_index])
"""




#a = multi_find("Ni! Ni! Ni! Ni!", "hi", 0, 20)
a = multi_find(4112341156411, 411, 0, 13)
print(a)
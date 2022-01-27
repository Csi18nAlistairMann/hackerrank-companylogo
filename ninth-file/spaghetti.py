#!/bin/python3

# Attempt to solve the Company Logo challenge at HackerRank:
# https://www.hackerrank.com/challenges/most-commons/problem

# This code less to solve the challenge but to demonstrate how the challenge
# was solved given I'm relatively new to Python3.

# My solution is to create an unsorted list of character frequencies in a dict,
# and then sort a separate list containing the dict's keys.

import imports
from setup import getInput
from processing import countThenAlphabeticSortPair2, countThenAlphabeticSort2, retrieveIntermediate1, doProcessing
from show_results import showResults

SHOW_NUM_RESULTS = 3

# Accept string from user (no santising done)
s = getInput()

# Create a python dict that associates individual characters to frequency of
# that character's appearance
intermediate1 = retrieveIntermediate1(s)
# Create a python list of the dict's keys, sorted per the requirements
intermediate2 = doProcessing(s, intermediate1)

# Provide results to user
showResults(SHOW_NUM_RESULTS, intermediate1, intermediate2)

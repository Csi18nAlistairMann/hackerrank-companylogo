#!/bin/python3

# After first parse of the requirements every single thing done is simply a comment for
# my own benefit. 
# 
# Notice that the requirements almost insist on Spaghetti Code: there's an input at the
# top of the code, processing in the middle, and output at the bottom. In a live program
# I'd start dividing those tasks up with subroutines.

# I'd put imports in imports.py then include that file. 
# start imports.py ==============
import math
import os
import random
import re
import sys
# end imports.py ==============

# start setup.py ==============
# This code would go in setup.py, would accept the input, and probably have an error
# check to make sure the constraints are valid. 
#
# Sample Input 0
# aabbbccde
if __name__ == '__main__':
    s = input()
# Constraints
# s "is the company name in lowercase letters" (assumes no unicode?)
# len(s) will be > 3 and <= 10^4
# s has at least 3 distinct characters
# end setup.py ==============


# start processing.py ==========
# Processing
# 1. Print the three most common characters 
#  - along with their occurrence count 
#  - each on a separate line.
# 2. Sort output in descending order of occurrence count.
#   2a. If the occurrence count is the same, sort the characters in alphabetical order.
# * * * * * * * 
# Part one:
# 1. Print the three most common characters 
#  - along with their occurrence count 
#  - each on a separate line.
# While there's almost certainly a clever way to only count the top three and so save
# CPU cycles, that's not what we've been asked so we're free to be inefficient! At this
# step it'd be sufficient to loop over the string examining each character in turn, and
# update some kind of intermediate record of what we found, ready for part 2.

# loop over S creating an intermediate record of occurrences.
for element in s:
    print(element, end=' ')
print("\n")

# What kind of intermediate record do we need? PHP allows, for instance, a 2D array such
# that we can have index 65 as the first element. Does python3? Can't remember! Just
# looking it seems the nearest equivalent would be a Python Dict - an associative array.
# With a dict, I believe the ascii (or unicode) value of the character is the index into
# the structure: data['a':6, 'b':2, ...]



# * * * * * * * 
# Part two:
# 2. Sort output in descending order of occurrence count.
#   2a. If the occurrence count is the same, sort the characters in alphabetical order.
# Now we take the intermediate record, and sort it first by occurences, with alphabetical
# order as a tie breaker. While the requirements say the user only wants the top three,
# I'll sort the whole thing through first.

# sort the intermediate record by occurence, alphabetic as a tie breaker

# end processing.py ==========

# start show-results.py ==========
# Sample Output 0
# b 3
# a 2
# c 2
# end show-results.py ==========


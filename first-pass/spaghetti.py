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
# end processing.py ==========

# start show-results.py ==========
# Sample Output 0
# b 3
# a 2
# c 2
# end show-results.py ==========


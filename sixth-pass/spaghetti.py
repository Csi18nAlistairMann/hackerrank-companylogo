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
# I cheated using https://docs.python.org/3/tutorial/datastructures.html
# I cheated using https://www.geeksforgeeks.org/iterate-over-characters-of-a-string-in-python/
intermediate1 = dict()
for element in s:
    if element in intermediate1:
        # I cheated using https://pythonguides.com/increment-and-decrement-operators-in-python/
        intermediate1[element] += 1
    else:
        # I cheated using https://www.tutorialspoint.com/python3/python_if_else.htm
        intermediate1[element] = 1
#    print(element, end=' ')
# I cheated using https://stackoverflow.com/questions/3294889/iterating-over-dictionaries-using-for-loops
# I cheated using https://stackoverflow.com/questions/1602934/check-if-a-given-key-already-exists-in-a-dictionary
#for key in intermediate1:
#    print (key, 'corresponds to', intermediate1[key])
#    print("\n")

# What kind of intermediate record do we need? PHP allows, for instance, a 2D array such
# that we can have index 65 as the first element. Does python3? Can't remember! Just
# looking it seems the nearest equivalent would be a Python Dict - an associative array.
# With a dict, I believe the ascii (or unicode) value of the character is the index into
# the structure: data['a':6, 'b':2, ...]

# sort the intermediate record. 
# Now I notice that python3's sort() doesn't seem to do what we want - by count and
# break ties by alphabetic. In fact it looks like only recent versions of python3 will
# sort dicts at all. We'd prefer to have code that older versions can run - so I'm
# going to write a custom sorter.
# I cheated using https://www.digitalocean.com/community/tutorials/how-to-define-functions-in-python-3
def countThenAlphabeticSortPair(intermediate_records, idx):
    keys_list = list(intermediate_records)
    key1 = keys_list[idx]    
    key2 = keys_list[idx + 1]
    val1 = intermediate_records[key1]
    val2 = intermediate_records[key2]
    if (val1 < val2):
        # We need to sort if the first item's count is lower than the second
        return True
    if (val1 == val2 and key1 > key2):
        # We need to sort if the first item's character is later than the second AND
        # the count is equal
        return True
    # Otherwise we don't need to sort at all
    return False

# test1 = {'a':6, 'b':3}
# if (countThenAlphabeticSortPair(test1, 0) == True):
#     print("Fail\n")
# else:
#     print("Success\n")

# test2 = {'a':3, 'b':6}
# if (countThenAlphabeticSortPair(test2, 0) == True):
#     print("Success\n")
# else:
#     print("Fail\n")

# test3 = {'a':6, 'b':6}
# if (countThenAlphabeticSortPair(test3, 0) == True):
#     print("Fail\n")
# else:
#     print("Success\n")

# test4 = {'b':6, 'a':6}
# if (countThenAlphabeticSortPair(test4, 0) == True):
#     print("Success\n")
# else:
#     print("Fail\n")

# I was going to swap key:value pairs in the dict but I suspect that's not allowed.
# Instead I'm going to create a 2nd intermediate record that is just a list of the
# characters in s; this then is referenced in accessing the original intermediate_record
# to discover if otherwise equal elements are sorted alphabetically.
intermediate2 = intermediate1.keys()
print(intermediate2)
print("-----------")

# We want to sort intermediate2 on the basis of the occurence in intermediate1. So
# now we use a second function to manage this. That is, intermediate1 doesn't get
# sorted at all - only intermediate2 does.
# I learned through trial and error that intermediate2, to be ordered, must be a
# list, while intermediate1 must be a dict, and therefore unsorted. This meant learning
# that lists get instantiated with [] whereas dicts with {}. How did this show up?
# By different test results every run because the dict was always in random order!
def countThenAlphabeticSortPair2(intermediateB, intermediateA, idx):
    keys_list = list(intermediateB)
    key1 = keys_list[idx]    
    key2 = keys_list[idx + 1]
    print(key1)
    print(key2)
    val1 = intermediateA[key1]
    val2 = intermediateA[key2]
    print(val1)
    print(val2)
    print("@@@@")
    if (val1 < val2):
        # We need to sort if the first item's count is lower than the second
        return True
    # I cheated using https://www.journaldev.com/23642/python-concatenate-string-and-int
    print("val1 " + str(val1))
    print("val2 " + str(val2))
    print("key1 " + key1)
    print("key2 " + key2)
    if (val1 == val2 and key1 > key2):
        # We need to sort if the first item's character is later than the second AND
        # the count is equal
        return True
    # Otherwise we don't need to sort at all
    return False

test1 = ['a', 'b']
testa = {'a':6, 'b':3}
if (countThenAlphabeticSortPair2(test1, testa, 0) == True):
    print("Fail\n")
else:
    print("Success\n")

test2 = ['a', 'b']
testb = {'a':3, 'b':6}
if (countThenAlphabeticSortPair2(test2, testb, 0) == True):
    print("Success\n")
else:
    print("Fail\n")

test3 = ['a', 'b']
testc = {'a':6, 'b':6}
if (countThenAlphabeticSortPair2(test3, testc, 0) == True):
    print("Fail\n")
else:
    print("Success\n")

test4 = ['b', 'a']
testd = {'b':6, 'a':6}
if (countThenAlphabeticSortPair2(test4, testd, 0) == True):
    print("Success\n")
else:
    print("Fail\n")



# def countThenAlphabeticSort(intermediate_records):
#     # This is a very simple sort: examine each pair of items and if they are unsorted
#     # swap them round and unset the sorted flag. Repeat as many times as needed until
#     # the scan looks over all the records without needing to swap any.
#     numRecords = len(intermediate_records)
#     # I cheated using https://www.w3schools.com/python/python_for_loops.asp
#     sortedF = False
#     while (sortedF == False):
#         # Keep looping through sorting until no sorting was done
#         sortedF = True
#         for idx in range(numRecords - 1):
#             # Don't sort the very last item as it has no pair! 
#             if (countThenAlphabeticSortPair(intermediate_records, idx) == True):
#                 tmp = intermediate_records[idx]
#                 intermediate_records[idx] = intermediate_records[idx + 1]
#                 intermediate_records[idx + 1] = tmp
#                 sortedF = False
#                 print("Sorted " + idx)
    
# intermediate2 = countThenAlphabeticSort(intermediate1)

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


# Create the dict - an associative array - that associates the frequency of a character
# with that character used as an index.
def retrieveIntermediate1(s):
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
        # I cheated using https://stackoverflow.com/questions/3294889/iterating-over-dictionaries-using-for-loops
        # I cheated using https://stackoverflow.com/questions/1602934/check-if-a-given-key-already-exists-in-a-dictionary
        #for key in intermediate1:
        #    print (key, 'corresponds to', intermediate1[key])
        #    print("\n")
    return intermediate1


# Create the list - a normal array - of all the keys in intermediate1 sorted as
# appropriate.
def doProcessing(s, intermediate1):
    # * * * * * * *
    # Part one:
    # 1. Print the three most common characters
    #  - along with their occurrence count
    #  - each on a separate line.
    # While there's almost certainly a clever way to only count the top three and so save
    # CPU cycles, that's not what we've been asked so we're free to be inefficient! At this
    # step it'd be sufficient to loop over the string examining each character in turn, and
    # update some kind of intermediate record of what we found, ready for part 2.

    # What kind of intermediate record do we need? PHP allows, for instance, a 2D array such
    # that we can have index 65 as the first element. Does python3? Can't remember! Just
    # looking it seems the nearest equivalent would be a Python Dict - an associative array.
    # With a dict, I believe the ascii (or unicode) value of the character is the index into
    # the structure: data['a':6, 'b':2, ...]

    # I was going to swap key:value pairs in the dict but I suspect that's not allowed.
    # Instead I'm going to create a 2nd intermediate record that is just a list of the
    # characters in s; this then is referenced in accessing the original intermediate_record
    # to discover if otherwise equal elements are sorted alphabetically.
    intermediate2 = intermediate1.keys()

    # * * * * * * *
    # Part two:
    # 2. Sort output in descending order of occurrence count.
    #   2a. If the occurrence count is the same, sort the characters in alphabetical order.
    # Now we take the intermediate record, and sort it first by occurences, with alphabetical
    # order as a tie breaker. While the requirements say the user only wants the top three,
    # I'll sort the whole thing through first.

    intermediate2 = countThenAlphabeticSort2(intermediate1)

    # intermediate2 is now a list of the characters, in occurrence order, then alphabetic order
    return intermediate2


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
    val1 = intermediateA[key1]
    val2 = intermediateA[key2]
    if (val1 < val2):
        # We need to sort if the first item's count is lower than the second
        return True
    # I cheated using https://www.journaldev.com/23642/python-concatenate-string-and-int
    # print("val1 " + str(val1))
    if (val1 == val2 and key1 > key2):
        # We need to sort if the first item's character is later than the second AND
        # the count is equal
        return True
    # Otherwise we don't need to sort at all
    return False


# Sort the intermediate record by occurence, alphabetic as a tie breaker
def countThenAlphabeticSort2(intermediate_records):
    # This is a very simple sort: examine each pair of items and if they are unsorted
    # swap them round and unset the sorted flag. Repeat as many times as needed until
    # the scan looks over all the records without needing to swap any.
    numRecords = len(intermediate_records)
    keys_list = list(intermediate_records)
    # I cheated using https://www.w3schools.com/python/python_for_loops.asp
    sortedF = False
    while (sortedF == False):
        # Keep looping through sorting until no sorting was done
        sortedF = True
        for idx in range(numRecords - 1):
            # Don't sort the very last item as it has no pair!
            if (countThenAlphabeticSortPair2(keys_list, intermediate_records, idx) == True):
                tmp = keys_list[idx]
                keys_list[idx] = keys_list[idx + 1]
                keys_list[idx + 1] = tmp
                sortedF = False
    return keys_list

# Sample Output 0
# b 3
# a 2
# c 2

# intermediate1 contains an unsorted dict of key:values where the key is
# a unique character and the value it's frequency in a given string.
# intermediate2 contains only the keys from the dict above, but these are
# sorted into the correct order.
#
# If we review the requirements we want to see only the top three results,
# along with their occurrences.
def showResults(show_num_results, intermediate1, intermediate2):
    for idx in range(show_num_results):
        key = intermediate2[idx]
        val = intermediate1[key]
        print(key + " " + str(val))

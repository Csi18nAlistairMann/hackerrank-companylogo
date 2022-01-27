# Sample Input 0
# aabbbccde
#
# Can't remember why this conditional is used. Something about use
# in a module rather than in the main file? Quite likely not needed
# at all here.
def getInput():
    if __name__ == 'setup':
        s = input()
    return s
#
# Constraints
# s "is the company name in lowercase letters" (assumes no unicode?)
# len(s) will be > 3 and <= 10^4
# s has at least 3 distinct characters

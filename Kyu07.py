
"""
This time no story, no theory. The examples below show you how to write function accum:
Examples:

accum("abcd")    # "A-Bb-Ccc-Dddd"
accum("RqaEzty") # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt")    # "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.

"""
def accum(iStr):
    return "-".join([iStr[c].upper()+(iStr[c]*c).lower() for c in range(len(iStr))])

"""
Given a string made of digits [0-9], return a string where each digit is repeated a number of times equals to its value.

Examples
explode("312") = "333122"
explode("102269") = "12222666666999999999"

"""
def explode(s):
    return "".join([c*int(c) for c in s])


"""
You might know some pretty large perfect squares. But what about the NEXT one?
Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. 
Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square, than -1 should be returned. You may assume the parameter is positive.

Examples:

findNextSquare(121) --> returns 144
findNextSquare(625) --> returns 676
findNextSquare(114) --> returns -1 since 114 is not a perfect
"""
def find_next_square(currSquare):
    retVal = -1
    root = int(currSquare ** 0.5)
    if root * root == currSquare:
        root += 1
        retVal = root * root

    return retVal

"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that 
determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. 
Ignore letter case.

is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case
"""

def is_isogram1(iStr):              # Original code
    retval = True
    if iStr > '':
        sStr = sorted(iStr.lower())
        for s in range(len(sStr) - 1):
            if sStr[s] == sStr[s + 1]:
                retval = False
                break

    return retval

def is_isogram(iStr):               # Refactored
    return len(iStr) == len(set(c for c in iStr.lower()))


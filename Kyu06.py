"""
Given two arrays a and b write a function comp(a, b) that checks whether the two arrays
have the "same" elements, with the same multiplicities. "Same" means, here, that the elements in b are the
elements in a squared, regardless of the order.

Examples
Valid arrays
    a = [121, 144, 19, 161, 19, 144, 19, 11]
    b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
    comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121, 20736 the square of 144,
    361 the square of 19, 25921 the square of 161, and so on. It gets obvious if we write b's elements in terms of squares:

a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
"""
def comp(arr1,arr2):

    if arr1 == None or arr2 == None:
        retVal = False
    elif len(arr1) == 0 and len(arr2) == 0:
        retVal = True
    else:
        retVal = sorted(set(x*x for x in arr1)) == sorted(set(arr2))

    return retVal

"""
Reverse or Rotate
The input is a string str of digits. Cut the string into chunks (a chunk here is a substring of the initial string) 
of size sz (ignore the last chunk if its size is less than sz).
If a chunk represents an integer such as the sum of the cubes of its digits is divisible by 2, reverse that chunk; 
otherwise rotate it to the left by one position. Put together these modified chunks and return the result as a string.

If sz is <= 0 or if str is empty return ""
sz is greater (>) than the length of str it is impossible to take a chunk of size sz hence return "".
"""

def revrot(strng, sz):
    chunks = []
    if sz > 0 and len(strng):
        chunks = [ strng[c:c+sz] for c in range(0,len(strng),sz) if len(strng[c:c+sz]) >= sz ]
        for pos,c in enumerate(chunks):
            chunks[pos] = c[::-1] if sum( int(d)**3 for d in c ) % 2 == 0 else c[1:]+c[0]

    return "".join(chunks)


"""
Your task is to sort a given string. Each word in the String will contain a single number. This number is the 
position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input String is empty, return an empty String. The words in the input String will only contain valid 
consecutive numbers. For an input: "is2 Thi1s T4est 3a" the function should return "Thi1s is2 3a T4est"

your_order("is2 Thi1s T4est 3a")
"Thi1s is2 3a T4est"
"""

def order(nStr):
    words = nStr.split()
    return " ".join([ w for n in range(1,len(words)+1) for w in words if str(n)in w])


"""
A stream of data is received and needs to be reversed. Each segment is 8 bits meaning the order of these segments 
need to be reversed:

11111111 00000000 00001111 10101010

(byte1) (byte2) (byte3) (byte4)

10101010 00001111 00000000 11111111

(byte4) (byte3) (byte2) (byte1)

Total number of bits will always be a multiple of 8. The data is given in an array as such:

[1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
"""


def data_reverse_orig(data):
    arr1 = [[data[int(y * 8 + x)] for x in range(0, 8)] for y in range(0, int(len(data) / 8))][::-1]
    arr2 = []
    for y in range(0, len(arr1)):
        for x in range(0, 8):
            arr2.append(arr1[y][x])

    return arr2

def data_reverse(data):
    arr1 = [[data[int(y * 8 + x)] for x in range(0, 8)] for y in range(0, int(len(data) / 8))][::-1]
    arr2 = [arr1[y][x] for y in range(0, len(arr1)) for x in range(0, 8)]

    return arr2

"""
Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.
"""
def expanded_form_orig(num):
    arr = []
    for i,x in enumerate(str(num)):
        if x != '0':
            arr.append(str(int(x)*10**(len(str(num))-i-1)))
    return " + ".join(arr)

def expanded_form(num):                     # refactored
    return " + ".join([str(int(x)*10**(len(str(num))-i-1)) for i,x in enumerate(str(num)) if x != '0' ])

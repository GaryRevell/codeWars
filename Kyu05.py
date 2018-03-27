"""
Create the function prefill that returns an array of n elements that all have the same value v.
See if you can do this without using a loop.

You have to validate input:

v can be anything (primitive or otherwise)
if v is ommited, fill the array with undefined
if n is 0, return an empty array
if n is anything other than an integer or integer-formatted string (e.g. '123') that is >=0, throw a TypeError
When throwing a TypeError, the message should be n is invalid, where you replace n for the actual value passed
to the function.

Code Examples

    prefill(3,1) --> [1,1,1]
    prefill(2,"abc") --> ['abc','abc']
    prefill("1", 1) --> [1]
    prefill(3, prefill(2,'2d')) --> [['2d','2d'],['2d','2d'],['2d','2d']]
"""

def prefill(n, v=None):
    try:
        retVar = [v] * (n if type(n) == int else int(n))
    except Exception as err:
        n = 'None' if n is None else n
        raise TypeError(n + " is invalid")

    return retVar


"""
Write a function nico/nico() that accepts two parameters:

key/$key - string consists of unique letters and digits
message/$message - string to encode
and encodes the message using the key.

First create a numeric key basing on a provided key by assigning each letter position in which it is located 
after setting the letters from key in an alphabetical order.

For example, for the key crazy we will get 23154 because of acryz (sorted letters from the key).
Let's encode secretinformation using our crazy key.

2 3 1 5 4
---------
s e c r e
t i n f o
r m a t i
o n
After using the key:

1 2 3 4 5
---------
c s e e r
n t i o f
a r m i t
  o n
"""

def nico(key, message):
    sortK = "".join(sorted(key))

    kLen = len(key)
    mLen = len(message)
    padLen = int(mLen / kLen)
    padLen = padLen if mLen % kLen == 0 else padLen + 1
    message = message.ljust(padLen * kLen, " ")
    chunks = [message[c:c + kLen] for c in range(0, len(message), kLen)]
    retStr = ""

    for w, word in enumerate(chunks):
        for k in sortK:
            col = key.find(k)
            c = word[col]
            retStr += word[col]

    return retStr


"""
How can you tell an extrovert from an introvert at NSA? Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it? 
According to Wikipedia, ROT13 (http://en.wikipedia.org/wiki/ROT13) is frequently used to obfuscate jokes on USENET.

Hint: For this task you're only supposed to substitue characters. Not spaces, punctuation, numbers etc. Test examples:

rot13("EBG13 rknzcyr.") == "ROT13 example.";
rot13("This is my first ROT13 excercise!" == "Guvf vf zl svefg EBG13 rkprepvfr!"
"""

def rot13(message):
    def enChar(char,offset):
        return chr(((ord(char) - offset + 13) % 26) + offset)
    retArr = []
    for c in message:
        if c.isupper():
            c=enChar(c,65)
        elif c.islower():
            c=enChar(c,97)
        retArr.append(c)
    return ''.join(retArr)

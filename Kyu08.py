
#
# Simple 8th Kyu functions
#

"""
It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string.
You're given one parameter, the original string. You don't have to worry with strings with less than two characters.
"""
def remove_char(s):
    return s[1:-1]      # skip the first and return upto but not including the last char

"""
Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
"""
def bool_to_word(boolean):
    return "Yes" if boolean == True else "No"

"""
You were camping with your friends far away from home, but when it's time to go back, you realize that you fuel 
is running out and the nearest pump is 50 miles away! You know that on average, your car runs on about 25 miles 
per gallon. There are 2 gallons left. Considering these factors, write a function that tells you if it is possible 
to get to the pump or not. Function should return true if it is possible and false if not.
"""
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left

"""
If a sperm cell containing an X chromosome fertilizes an egg, the resulting zygote will be XX or female. 
If the sperm cell contains a Y chromosome, then the resulting zygote will be XY or male. Determine if the sex of 
the offspring will be male or female based on the X or Y chromosome present in the male's sperm.

If the sperm contains the X chromosome, return "Congratulations! You're going to have a daughter."; 
If the sperm contains the Y chromosome, return "Congratulations! You're going to have a son.";
"""
def chromosome_check(chromosomes):
    return format("Congratulations! You're going to have a {}.".format("son" if chromosomes[1] == "Y" else "daughter"))

#
# Test functions & data.
# Each test function sets up test data (not exhaustive!) and then calls the function being tested for each test case
#

def test_remove_char():
    tests = [['eloquent' , 'loquen'] , ['country' , 'ountr' ],
             ['person' , 'erso' ], ['place' , 'lac'],
             ['ok' , '' ], ['QWERTYUIOP' , "WERTYUIO" ],
             ['False','Fals']]              # for remove_char(s)
    for i,t in tests:
        print(i,"=>",t, "is" ,t == remove_char(i))

def test_bool_to_word():
    tests = [[True,'Yes'],[False,'No']]
    for bool,t in tests:
        print(bool,"=>",t,bool_to_word(bool) == t)

def test_zero_fuel():
    tests = [[50,25,2,True],[100,50,1,False],[300,33,9.5,True]]
    for dist,mpg,fuel,valid in tests:
        print("{} miles to go at an mpg {} with {} gallons left : Make it = {}".format(dist,mpg,fuel,zero_fuel(dist,mpg,fuel)))

def test_chromosome_check():
    for x in ['XX','XY']:
        print(x,chromosome_check(x))

#
# Test driver to execute each test function.
# Create a list of functions to be tested and then execute the relevant test_ function
#
testFuncs = [remove_char,bool_to_word,zero_fuel,chromosome_check]
for f in testFuncs:
    print("\nRunning tests for",f.__name__)
    eval("test_{}()".format(f.__name__))

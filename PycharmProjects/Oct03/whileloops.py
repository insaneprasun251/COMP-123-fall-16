""" ==================================================
File: whileloops.py
Author: Susan Fox
Date:  Spring 2013

This file contains examples of while and for loops for the Iteration
activity.  """


# ====================================================
# Simple while loop examples

# loop 1
def printEveryFifth(x):
    """One input x: must be an integer >= 0
    Prints every 5th value from x down to zero"""
    while x >= 0:   # x is the loop variable
        print(x)
        x = x - 5
    # when indentation stops, while loop is over
    print("Done!")
# end of printEveryFifth

print("------------------------------")
print("Sample calls to printEveryFifth:")
print("printEveryFifth(10) does:")
printEveryFifth(10)
print("printEveryFifth(4) does:")
printEveryFifth(4)

# printEveryOther counts down from the input number by 2, for positive numbers only
# printEveryFifth does the same but by 5


def squareUserNums():
    # Initialize loop variable 
    userInp = input("Enter the next number (negative to quit): ")
    userNum = int(userInp)
    while userNum >= 0:
        print(userNum, "squared is", userNum ** 2)
        userInp = input("Enter the next number (negative to quit): ")
        userNum = int(userInp)


#squareUserNums()

# with first 2 lines commented out the f'n doesn't work because the loop variables haven't been initialized
# with the two lines in the loop commented out it repeats forever because there's no change in the loop condition
    
        
def sum3s(topNum):
    currVal = 0  # loop variable
    total = 0    # accumulator variable
    while currVal <= topNum:
        print(currVal, "\t", total)
        total = total + currVal
        currVal = currVal + 3
    return total

# sum3s sums multiples of three up to the user input value

sum3s(20)


def adduserNums():
    """adds numbers entered by the user until a negative is encountered."""
    userNum = 0
    accum = 0
    while userNum >= 0:
        userInp = input("enter a number (negative to quit): ")
        userNum = int(userInp)
        accum = accum + userNum
    print(accum)
    return accum

adduserNums()



def cappedTotal(numList):
    """Takes in a list of numbers and adds the numbers up.  
If it gets to a result that is more than 100, then the loop 
stops and it returns 100"""
    total = 0
    for val in numList:
        total = total + val
        if total > 100:
            total = 100
            break
        # end if statement
    # end for loop
    return total


def squareUserNumsTwo():
    """edited copy of squareUserNums using if and a break to shorten it."""
    while True:
        userInp = input("Enter the next number (negative to quit): ")
        userNum = int(userInp)
        if userNum < 0:
            break
        print(userNum, "squared is", userNum ** 2)

squareUserNumsTwo()
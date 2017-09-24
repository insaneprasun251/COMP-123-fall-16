# Part One


def printPairs(n, m):
    """Prints all pairs of values from 0 to n-1 with values from 0 to m-1"""
    for i in range(n):
        for j in range(m):
            print("(", i, j, ")")

printPairs(2, 3)

# Returns
# (0,0)
# (0,1)
# (0,2)
# (1,0)
# (1,1)
# (1,2)
# The loop for n runs one step through and steps through all iterations of the loop for n.
# Next the loop for m runs all iterations on the second time through loop n.

# Part Two

import turtle

tu = turtle.Turtle()
wn = turtle.Screen()


def nestedSquares(turt):
    """draws 8 nested squares"""
    for i in range(10, 80, 10):
        for j in range(4):
            turt.fd(i)
            turt.lt(90)

#nestedSquares(tu)

wn.exitonclick()

# part Three


def sumRange(startVal, endVal):
    cnt = 0 # Initialize accumulator to default count of 0
    for x in range(startVal, endVal+1):
        cnt = cnt + x   # add the new value of x to the old value of cnt,
    return cnt

print(sumRange(1, 6))    # returns 21: the sum of 1, 2, 3, 4, 5, 6
print(sumRange(4, 4))    # returns 9: the sum of 4, 5? actually returns 4—-range of for loop is still only 1
print(sumRange(20, 15))  # returns 0: range is 0 because we've written it to only work in one direction
print(sumRange(-4, -2))  # returns -9: sum of -4,-3,-2

# Part Four


def copyStr(string, numTimes):
    ansStr = ""  # initialize accumulator to default value
    for x in range(numTimes):
        ansStr = ansStr + string  # add to accumulator another copy of string
        print(ansStr)
    return ansStr

copyStr("pqrs", 4)

# copyStr adds the input string to itself numTimes with the same accumulator pattern we used above, but with
# string addition instead of math

# Part Five


def stringOfNums(input):
    output = "" # initialize accumulator to default value
    for i in range(1, input + 1):
        output = output + str(i) + " "
    return output

print(stringOfNums(10))

# Part Six, Seven

import decimal


def rectArea(length, width):
    lengthUp = decimal.ROUND_UP(length)
    widthUp = decimal.ROUND_UP(width)
    area = lengthUp * widthUp
    return area


def roofCost(area, price):
    totalCost = area * price
    return totalCost

print(roofCost(rectArea(54.25, 32.8), 1))

from inclass_solutions import *

#change the import statement above to match your solution file's name

import turtle

# ==========================================================================================
# Basic test to see if you have configured the test file correctly
# Note: homeworks will not have a trivial test like this


def importTest():
    print("--------------------------------------")
    print("Testing the import statement:")
    if ready != "dog":
        print ("expected a variable named ready with value dog. A variable was found (indicating a successful import) but the value was not dog")
        print("the value of the variable named ready is", ready)
    else:
        print ("Tests OK")
    print("--------------------------------------")

# uncomment to test import
importTest()

# ==========================================================================================
# Tests for fourStairs

def dubSqrRootTest():
    print("--------------------------------------")
    print("Testing dubSqrRoot:")

    v0 = dubSqrRoot(0)
    v1 = dubSqrRoot(4)
    v2 = dubSqrRoot(8)
    v3 = dubSqrRoot(123.4)

    allOk = True
    if v0 != 0:
        print("Called: dubSqrRoot(0)")
        print("Expected 0 but function returned", v0)
        allOk = False
    if v1 != 2:
        print("Called: dubSqrRoot(4)")
        print("Expected 2 but function returned", v1)
        allOk = False
    if v2 != 4:
        print("Called: dubSqrRoot(8)")
        print("Expected 4 but function returned", v2)
        allOk = False
    if v3 != 15:
        print("Called: dubSqrRoot(123.4)")
        print("Expected 15 but function returned", v3)
        allOk = False
    if allOk:
        print("Tests Ok")
    print("--------------------------------------")


# Remove the # from the following line to run the test for dubSqrRoot
dubSqrRootTest()


# ==========================================================================================
# Tests for square

def squareTest():
    print("--------------------------------------")
    print("Testing square:")

    win1 = turtle.Screen()
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    t2.up()
    t2.goto(-300, 0)
    t2.color('red')
    t2.down()
    square(t1)
    square(t2)

    print("    Check this one visually, should see two squares, a black set a red set to the left.")
    print("    Both squares should be the same size")
    win1.exitonclick()

    print("--------------------------------------")


# Remove the # from the following line to run the test for square
squareTest()


# ==========================================================================================
# Tests for largePrime

def largePrimeTests():
    print("--------------------------------------")
    print("Testing largePrime:")

    allOk = True

    v1 = largePrime(10) #3628801
    v2 = largePrime(1) #2
    v3 = largePrime(22) #
    if v1 != 3628801:
        print("Called: largePrime(10)")
        print("Expected 3628801 but function returned", v1)
        allOk = False
    if v2 != 2:
        print("Called: largePrime(1)")
        print("Expected 2 but function returned", v2)
        allOk = False
    if v3 != 1124000727777607680001:
        print("Called: largePrime(22)")
        print("Expected 1124000727777607680001 but function returned", v3)
        allOk = False
    if allOk:
        print("Tests Ok")
    print("--------------------------------------")


# Remove the # from the following line to run the test for largePrime
largePrimeTests()


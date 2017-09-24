

# put import statements here
import turtle
import random

# Question 1

# put your solution here


def fourStairs(tu):
    """turtle draws stairs"""
    for i in range(4):
        tu.lt(90)
        tu.fd(25)
        tu.rt(90)
        tu.fd(40)
    tu.rt(90)
    tu.fd(100)
    tu.rt(90)
    tu.fd(160)



# Question 2

# put your solution here


def nStairs(tu,numStairs):
    """turtle draws n stairs"""
    for i in range(numStairs):
        tu.lt(90)
        tu.fd(25)
        tu.rt(90)
        tu.fd(40)
    tu.rt(90)
    tu.fd(25*numStairs)
    tu.rt(90)
    tu.fd(40*numStairs)



# Question 3

# put your solution here


def rollDice(numDice):
    """rolls numDice dice"""
    accum = 0
    for i in range(numDice):
        accum = accum + random.randint(1,6)
    return accum



# Question 4

# put your solution here


def printNMults(multiple, n):
    """prints n multiples of multiple"""
    for q in range(0, n+1):
        print(multiple * q)

printNMults(2, 5)


# Question 5


# put your definition of flower here, before the petal function.

def flower(turt, numPetals, angle):
    for i in range(numPetals):
        petal(turt)
        turt.rt(angle)




def petal(bobT):
    """Takes in a turtle object, and draws a single petal in the direction the turtle is
    currently facing, and going to the left of that point"""
    bobT.begin_fill()
    bobT.forward(150)
    bobT.left(50)
    bobT.forward(40)
    bobT.left(100)
    bobT.forward(40)
    bobT.left(50)
    bobT.forward(150)
    bobT.end_fill()
    bobT.left(160)
    

# ====================================================================
#  COMP 123 Homework 3
#  <put your name and section here>
# ====================================================================

# <put import statements here>
import random

# ==============================================================
# Question 1

# Put your definition of timeChange() below here


def timeChange():
    """changes time forward or backward by user input increments"""
    inHr = int(input("Enter the current hour"))
    inMin = int(input("Enter the current minute"))
    changeHr = int(input("Enter the change in hours"))
    changeMin = int(input("Enter the change in minutes"))
    changeDir = input("Change time forward (f) or backward (b)?")

    if changeDir == "f":
        outHr = (inMin + changeMin) // 60 + (inHr + changeHr) % 24
        outMin = (inMin + changeMin) % 60
    elif changeDir == "b":
        outHr = (inMin - changeMin) // 60 + (inHr - changeHr) % 24
        outMin = (inMin - changeMin) % 60
    else:
        pass
    print("The new time is: ", outHr, "hr and", outMin, "minutes")




    

# ==============================================================
# Question 2


def followPath(turt, inStr, dist=20, angle=90):
    """makes turtle move specified distance and angles according to input string where F = forward,
    B = backward, r = right, l = left, and j = move without drawing a line."""
    for chars in inStr:
        if chars == "F":
            turt.fd(dist)
        elif chars == "B":
            turt.bk(dist)
        elif chars == "R":
            turt.rt(angle)
        elif chars == "L":
            turt.lt(angle)
        elif chars == "J":
            turt.up()
            turt.fd(dist)
            turt.down()
        else:
            pass

# ==============================================================
# Question 3

def randAddN(n):
    """Takes in a number, n, and randomly generates numbers between 1 and 20 until they add up
    to more than n.  It prints the random number each time, and prints a summary of how many numbers
    and the actual final sum"""
    total = 0
    count = 0
    while total <= n:
      nextNum = random.randrange(1, 21)         # randint doesn't work. should be random.randrange(1, 21)
      print("Next number:", nextNum)
      total = total + nextNum
      count = count + 1                         # count needs to increase by 1 each time.
    print("Added", count, "random numbers to reach", total)      # needs comma after count


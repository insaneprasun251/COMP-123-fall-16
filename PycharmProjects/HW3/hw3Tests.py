# ====================================================================
#
#  Homework 3 tests
#
# ====================================================================

# Change the filename below to match your solution file's name

from hw3Code import *

import turtle
import random
import time


# ========================================================================
# Main tester function. I created this so you only have to make changes
# to this file up here at the top.


def runTests():
    """Uncomment the tests here that you want to run."""
    timeChangeTests()
    testFollowPath()
    randAddNTests()

    print("DONE WITH ALL TESTS.")


# ==========================================================================================
# Tests for timeChange

def timeChangeTests():
    print("--------------------------------------")
    print("Testing timeChange:    ")

    option = "y"
    while option == "y":
        timeChange()
        option = input("Would you like to enter another time (y/n): ")
    print("""Check manually: Use the examples given in the homework writeup
            and ones that you create""")
    print("--------------------------------------")

# ==========================================================================================
# Tests for followPath

def testFollowPath():
    print("--------------------------------------")
    print("Testing followPath:       CHECK VISUALLY")

    sss = turtle.Screen()
    sss.bgcolor('lightblue')
    ttt = turtle.Turtle()
    ttt.speed(0)
    followPath(ttt, "FFFFFL FFFFFFFL FFFFFL FFFFFFFL JJLJ FFFR FFR FFFR FFR")
    #sss.exitonclick()

    time.sleep(2)
    sss.clear()

    sss.bgcolor('black')
    ttt = turtle.Turtle()
    ttt.speed(0)
    cols = ['red', 'blue', 'green', 'yellow', 'pink', 'orange', 'cyan']
    followPath(ttt, "JJJ R JJJ L ignores the rest fblrj", -100)
    for col in cols:
        ttt.color(col)
        followPath(ttt, "FLFRFR FLFRFR FLFRFR FLFRFR")
        followPath(ttt, "JJumpump JJumpump")
    ttt.color("white")
    followPath(ttt, "JJ L JJJ R", -150)
    for d in range(10, 51, 5):
        followPath(ttt, "FFL-" * 8, d, 45)

    sss.exitonclick()

    print("    Two windows:")
    print("      First: rectangle drawn counterclockwise, with a smaller rectangle clockwise inside")
    print("      Second: Black background, 7 T shapes near top, nested octagons in lower middle")
    print("--------------------------------------")
    input("Press a key to go on: ")


# ==========================================================================================
# Tests for randAddN

def randAddNTests():
    print("--------------------------------------")
    print("Testing randAddN:")

    randAddN(50)
    randAddN(50)
    randAddN(50)
    randAddN(100)
    randAddN(100)
    randAddN(100)

    print("""Check manually: should take about 4-6 to add up to 50 or more, and about 10
    to add up to 100 or more""")
    print("--------------------------------------")

runTests()


# Change the filename below to match your solution file's name
#from hw2Code import *
from hw2Code import *

import turtle
import tkinter

def newScreen():
    """ complicated function that allows us to have mutiple turtle screens """
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, width=800, height=800)
    canvas.pack()
    sc = turtle.TurtleScreen(canvas)
    def bye(e):
        root.destroy()
    def exitonclick():
        canvas.bind("<Button-1>", bye)
        root.mainloop()
    sc.exitonclick = exitonclick
    return sc
# ==========================================================================================
# Tests for fourStairs

def fourStairsTests():
    print("--------------------------------------")
    print("Testing fourStairs:")

    win1 = newScreen()
    t1 = turtle.RawTurtle(win1)
    t1.speed(0)
    t2 = turtle.RawTurtle(win1)
    t2.speed(0)
    t2.up()
    t2.goto(-250, 0)
    t2.color('red')
    t2.down()
    fourStairs(t1)
    fourStairs(t2)
    win1.exitonclick()
    print("    Check this one visually, should see two stairs, a black set starting")
    print("    in the middle and a red set starting to the left.")
    print("--------------------------------------")    

# Remove the # from the following line to run the test for fourStairs
fourStairsTests()


# ==========================================================================================
# Tests for nStairs

def nStairsTests():
    print("--------------------------------------")
    print("Testing nStairs:")
    
    win1 = newScreen()
    t3 = turtle.RawTurtle(win1)
    t3.speed(0)
    t4 = turtle.RawTurtle(win1)
    t4.speed(0)
    t4.up()
    t4.goto(-300, 0)
    t4.color('red')
    t4.down()
    nStairs(t3, 2)
    nStairs(t4, 6)
    win1.exitonclick()
    
    print("    Check this one visually, should see two stairs, a black set with 2 steps starting")
    print("    in the middle and a red set with six steps starting to the left.")
    print("--------------------------------------")    
        

# Remove the # from the following line to run the test for nStairs
nStairsTests()

    
# ==========================================================================================
# Tests for rollDice

def rollDiceTests():
    print("--------------------------------------")
    print("Testing rollDice:")
    
    # testing a code that has random return values is hard. we can predict a specific range that the output should
    # be in and test that many times. This is not a perfect test, but its a good start.
    allOk = True

    out = rollDice(0)
    if out != 0:
        print("Called rollDice(0)")
        print("Expected:", 0, "but function returned", out)
        allOk = False
    
    for i in range(100):
        out = rollDice(1)
        if out < 1 or out > 6:
            print("Called: rolDice(1)")
            print("Expected a number between 1 and 6 but function returned", out)
            allOk = False
            break # this makes it stop testing the first time it fails.

    for i in range(100):
        out = rollDice(13)
        if out < 13 or out > 13*6:
            print("Called: rolDice(13)")
            print("Expected a number between 13 and 78 but function returned", out)
            allOk = False
            break # this makes it stop testing the first time it fails.
        
    if allOk:
        print("Tests Ok")
    print("--------------------------------------")    
    
# Remove the # from the following line to run the test for binStrToInt
rollDiceTests()
   

# ==========================================================================================
# Tests for flower

def flowerTests():
    print("--------------------------------------")
    print("Testing flower:")
    
    win1 = newScreen()
    t1 = turtle.RawTurtle(win1)
    t1.speed(0)
    t1.color('magenta')
    t1.up()
    t1.goto(-300, -200)
    t1.down()
    flower(t1, 8, 45)

    t1.color('blue')
    t1.up()
    t1.goto(50, 0)
    t1.down()
    t1.setheading(0)
    flower(t1, 9, 40)

    t1.color('green')
    t1.up()
    t1.goto(275,275)
    t1.down()
    t1.setheading(0)
    flower(t1, 4, 30)

    win1.exitonclick()
    
    print("    Check this one visually, should see first a magenta flower with 8 petals,")
    print("    and then a blue one with nine petals, and finally a partial flower,")
    print("    green with four petals.")
    print("--------------------------------------")    
        

# Remove the # from the following line to run the test for nStairs
flowerTests()

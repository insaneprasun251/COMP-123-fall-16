# In python, anything after a hash mark `#` is ignored.
# This feature is designed to allow human readable comments.

# This file uses the "turtle module" which will be introduced next week to draw things.

# At this point you are not expected to understand this file.
# By the end of this class you should understand what each part of it does.
import turtle

window = turtle.Screen()
myTurtle = turtle.Turtle()
myTurtle.speed(0)

alex = turtle.Turtle()
alex.speed(0)
alex.pensize(4)

window.bgcolor("lavender")
myTurtle.color("red")
for i in range(1,400):
    myTurtle.forward(i)
    myTurtle.right(90 - 90 / i)
    # alex.forward(i)
    # alex.left(90 - 90 / i)
window.exitonclick()
import turtle
import math

win = turtle.Screen()
win.bgcolor("red")

turtleA = turtle.Turtle()
turtleA.speed(6)
turtleA.color("navy")

turtleB = turtle.Turtle()
turtleB.speed(6)
turtleB.color("darkorange")

turtleC = turtle.Turtle()
turtleC.speed(6)
turtleC.color("navy")

turtleD = turtle.Turtle()
turtleD.speed(6)
turtleD.color("darkorange")

turtleE = turtle.Turtle()
turtleE.speed(6)
turtleE.color("navy")
turtleE.shape("turtle")

turtleA.up()
turtleA.goto(-50, -round(100 * (1 + math.sqrt(2)) / 2))
turtleA.down()

turtleA.begin_fill()

for i in range(8):
    turtleA.forward(100)
    turtleA.left(45)

turtleA.end_fill()

turtleA.hideturtle()

turtleB.up()
turtleB.goto(-32, -round(64 * (1 + math.sqrt(2)) / 2))
turtleB.down()

turtleB.begin_fill()
# This can be replaced with our first for loop again.
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.end_fill()

turtleB.hideturtle()

turtleC.up()
turtleC.goto(-18, -round(36 * (1 + math.sqrt(2)) / 2))
turtleC.down()

turtleC.begin_fill()
# This can be replaced with our first for loop again.
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.end_fill()

turtleC.hideturtle()

turtleD.up()
turtleD.goto(-8, -round(16 * (1 + math.sqrt(2)) / 2))
turtleD.down()

turtleD.begin_fill()
# This can be replaced with our first for loop again.
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.end_fill()

turtleD.hideturtle()

turtleE.up()
turtleE.goto(-2, 0)
turtleE.down()
turtleE.stamp()

turtleA.showturtle()
turtleA.up()
turtleA.goto(-50, 250 - round(100 * (1 + math.sqrt(2)) / 2))
turtleA.down()

turtleA.begin_fill()
# This can be replaced with our first for loop again.
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.end_fill()

turtleA.hideturtle()

turtleB.showturtle()
turtleB.up()
turtleB.goto(-32, 250 - round(64 * (1 + math.sqrt(2)) / 2))
turtleB.down()

turtleB.begin_fill()
# This can be replaced with our first for loop again.
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.end_fill()

turtleB.hideturtle()

turtleC.showturtle()
turtleC.up()
turtleC.goto(-18, 250 - round(36 * (1 + math.sqrt(2)) / 2))
turtleC.down()

turtleC.begin_fill()
# This can be replaced with our first for loop again.
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.end_fill()

turtleC.hideturtle()

turtleD.showturtle()
turtleD.up()
turtleD.goto(-8, 250 - round(16 * (1 + math.sqrt(2)) / 2))
turtleD.down()

turtleD.begin_fill()
# This can be replaced with our first for loop again.
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.end_fill()

turtleD.hideturtle()

turtleE.up()
turtleE.goto(-2, 250)
turtleE.down()
turtleE.stamp()

turtleA.showturtle()
turtleA.up()
turtleA.goto(-50, -250 - round(100 * (1 + math.sqrt(2)) / 2))
turtleA.down()

turtleA.begin_fill()
# This can be replaced with our first for loop again.
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.end_fill()

turtleA.hideturtle()

turtleB.showturtle()
turtleB.up()
turtleB.goto(-32, -250 - round(64 * (1 + math.sqrt(2)) / 2))
turtleB.down()

turtleB.begin_fill()
# This can be replaced with our first for loop again.
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.end_fill()

turtleB.hideturtle()

turtleC.showturtle()
turtleC.up()
turtleC.goto(-18, -250 - round(36 * (1 + math.sqrt(2)) / 2))
turtleC.down()

turtleC.begin_fill()
# This can be replaced with our first for loop again.
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.end_fill()

turtleC.hideturtle()

turtleD.showturtle()
turtleD.up()
turtleD.goto(-8, -250 - round(16 * (1 + math.sqrt(2)) / 2))
turtleD.down()

turtleD.begin_fill()
# This can be replaced with our first for loop again.
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.end_fill()

turtleD.hideturtle()

turtleE.up()
turtleE.goto(-2, -250)
turtleE.down()
turtleE.stamp()

turtleA.showturtle()
turtleA.up()
turtleA.goto(250 - 50, 250 - round(100 * (1 + math.sqrt(2)) / 2))
turtleA.down()

turtleA.begin_fill()
# This can be replaced with our first for loop again.
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.end_fill()

turtleA.hideturtle()

turtleB.showturtle()
turtleB.up()
turtleB.goto(250 - 32, 250 - round(64 * (1 + math.sqrt(2)) / 2))
turtleB.down()

turtleB.begin_fill()
# This can be replaced with our first for loop again.
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.end_fill()

turtleB.hideturtle()

turtleC.showturtle()
turtleC.up()
turtleC.goto(250 - 18, 250 - round(36 * (1 + math.sqrt(2)) / 2))
turtleC.down()

turtleC.begin_fill()
# This can be replaced with our first for loop again.
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.end_fill()

turtleC.hideturtle()

turtleD.showturtle()
turtleD.up()
turtleD.goto(250 - 8, 250 - round(16 * (1 + math.sqrt(2)) / 2))
turtleD.down()

turtleD.begin_fill()
# This can be replaced with our first for loop again.
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.end_fill()

turtleD.hideturtle()

turtleE.up()
turtleE.goto(250 - 2, 250)
turtleE.down()
turtleE.stamp()

turtleA.showturtle()
turtleA.up()
turtleA.goto(- 250 - 50, 250 - round(100 * (1 + math.sqrt(2)) / 2))
turtleA.down()

turtleA.begin_fill()
# This can be replaced with our first for loop again.
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.end_fill()

turtleA.hideturtle()

turtleB.showturtle()
turtleB.up()
turtleB.goto(- 250 - 32, 250 - round(64 * (1 + math.sqrt(2)) / 2))
turtleB.down()

turtleB.begin_fill()
# This can be replaced with our first for loop again.
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.end_fill()

turtleB.hideturtle()

turtleC.showturtle()
turtleC.up()
turtleC.goto(- 250 - 18, 250 - round(36 * (1 + math.sqrt(2)) / 2))
turtleC.down()

turtleC.begin_fill()
# This can be replaced with our first for loop again.
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.end_fill()

turtleC.hideturtle()

turtleD.showturtle()
turtleD.up()
turtleD.goto(- 250 - 8, 250 - round(16 * (1 + math.sqrt(2)) / 2))
turtleD.down()

turtleD.begin_fill()
# This can be replaced with our first for loop again.
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.end_fill()

turtleD.hideturtle()

turtleE.up()
turtleE.goto(- 250 - 2, 250)
turtleE.down()
turtleE.stamp()

turtleA.showturtle()
turtleA.up()
turtleA.goto(250 - 50, -round(100 * (1 + math.sqrt(2)) / 2))
turtleA.down()

turtleA.begin_fill()
# This can be replaced with our first (for loop) again.
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.end_fill()

turtleA.hideturtle()

turtleB.showturtle()
turtleB.up()
turtleB.goto(250 - 32,  - round(64 * (1 + math.sqrt(2)) / 2))
turtleB.down()

turtleB.begin_fill()
# This can be replaced with our first (for loop) again.
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.end_fill()

turtleB.hideturtle()

turtleC.showturtle()
turtleC.up()
turtleC.goto(250 - 18, - round(36 * (1 + math.sqrt(2)) / 2))
turtleC.down()

turtleC.begin_fill()
# This can be replaced with our first (for loop) again.
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.end_fill()

turtleC.hideturtle()

turtleD.showturtle()
turtleD.up()
turtleD.goto(250 - 8, - round(16 * (1 + math.sqrt(2)) / 2))
turtleD.down()

turtleD.begin_fill()
# This can be replaced with our first (for loop) again.
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.end_fill()

turtleD.hideturtle()

turtleE.up()
turtleE.goto(250 - 2, 0)
turtleE.down()
turtleE.stamp()

turtleA.showturtle()
turtleA.up()
turtleA.goto(- 250 - 50, - round(100 * (1 + math.sqrt(2)) / 2))
turtleA.down()

turtleA.begin_fill()
# This can be replaced with our first (for loop) again.
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.end_fill()

turtleA.hideturtle()

turtleB.showturtle()
turtleB.up()
turtleB.goto(- 250 - 32, - round(64 * (1 + math.sqrt(2)) / 2))
turtleB.down()

turtleB.begin_fill()
# This can be replaced with our first (for loop) again.
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.end_fill()

turtleB.hideturtle()

turtleC.showturtle()
turtleC.up()
turtleC.goto(- 250 - 18, - round(36 * (1 + math.sqrt(2)) / 2))
turtleC.down()

turtleC.begin_fill()
# This can be replaced with our first (for loop) again.
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.end_fill()

turtleC.hideturtle()

turtleD.showturtle()
turtleD.up()
turtleD.goto(- 250 - 8, - round(16 * (1 + math.sqrt(2)) / 2))
turtleD.down()

turtleD.begin_fill()
# This can be replaced with our first (for loop) again.
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.end_fill()

turtleD.hideturtle()

turtleE.up()
turtleE.goto(- 250 - 2, 0)
turtleE.down()
turtleE.stamp()

turtleA.showturtle()
turtleA.up()
turtleA.goto(250 - 50, -250 - round(100 * (1 + math.sqrt(2)) / 2))
turtleA.down()

turtleA.begin_fill()
# This can be replaced with our first (for loop) again.
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.end_fill()

turtleA.hideturtle()

turtleB.showturtle()
turtleB.up()
turtleB.goto(250 - 32, -250 - round(64 * (1 + math.sqrt(2)) / 2))
turtleB.down()

turtleB.begin_fill()
# This can be replaced with our first (for loop) again.
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.end_fill()

turtleB.hideturtle()

turtleC.showturtle()
turtleC.up()
turtleC.goto(250 - 18, -250 - round(36 * (1 + math.sqrt(2)) / 2))
turtleC.down()

turtleC.begin_fill()
# This can be replaced with our first (for loop) again.
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.end_fill()

turtleC.hideturtle()

turtleD.showturtle()
turtleD.up()
turtleD.goto(250 - 8, -250 - round(16 * (1 + math.sqrt(2)) / 2))
turtleD.down()

turtleD.begin_fill()
# This can be replaced with our first (for loop) again.
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.end_fill()

turtleD.hideturtle()

turtleE.up()
turtleE.goto(250 - 2, -250)
turtleE.down()
turtleE.stamp()

turtleA.showturtle()
turtleA.up()
turtleA.goto(-250 - 50, -250 - round(100 * (1 + math.sqrt(2)) / 2))
turtleA.down()

turtleA.begin_fill()
# This can be replaced with our first (for loop) again.
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.forward(100)
turtleA.left(45)
turtleA.end_fill()

turtleA.hideturtle()

turtleB.showturtle()
turtleB.up()
turtleB.goto(-250 - 32, -250 - round(64 * (1 + math.sqrt(2)) / 2))
turtleB.down()

turtleB.begin_fill()
# This can be replaced with our first (for loop) again.
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.forward(64)
turtleB.left(45)
turtleB.end_fill()

turtleB.hideturtle()

turtleC.showturtle()
turtleC.up()
turtleC.goto(-250 - 18, -250 - round(36 * (1 + math.sqrt(2)) / 2))
turtleC.down()

turtleC.begin_fill()
# This can be replaced with our first (for loop) again.
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.forward(36)
turtleC.left(45)
turtleC.end_fill()

turtleC.hideturtle()

turtleD.showturtle()
turtleD.up()
turtleD.goto(-250 - 8, -250 - round(16 * (1 + math.sqrt(2)) / 2))
turtleD.down()

turtleD.begin_fill()
# This can be replaced with our first (for loop) again.
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.forward(16)
turtleD.left(45)
turtleD.end_fill()

turtleD.hideturtle()

turtleE.up()
turtleE.goto(-250 - 2, -250)
turtleE.down()
turtleE.stamp()

win.exitonclick()

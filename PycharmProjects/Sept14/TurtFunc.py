#Part Five
import turtle

window = turtle.Screen()
foo = turtle.Turtle()
bar = turtle.Turtle()
qwe = turtle.Turtle()
asd = turtle.Turtle()

foo.color("black")
bar.color("blue")
qwe.color("red")
asd.color("green")

def triangle(turtle, length):
    """Makes a turtle 'turtle' draw an equilateral triangle with side length 'length'"""

    for i in range(3):
        turtle.fd(length)
        turtle.left(120)

#Part Six

triangle(foo, 50)
triangle(bar,100)
triangle(qwe, 150)
triangle(asd,200)


#Part Seven

for i in range(19):
    triangle(foo, 100)
    foo.rt(20)
    foo.fd(10)

def drawPoly(turt, length, numSides):
    """Makes turtle 'turt' draw a polygon with 'numSides' sides and side length 'length'"""
    for i in range(numSides):
        turt.fd(length)
        turt.rt(360/numSides)

drawPoly(asd, 12, 17)

window.exitonclick()

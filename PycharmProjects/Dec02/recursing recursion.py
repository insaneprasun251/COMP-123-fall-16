import turtle
import math

sc = turtle.Screen()
bob = turtle.Turtle()
bob.speed(0)


def spiral(turt, length):
    if length <= 5:
        pass
    else:
        turt.fd(length)
        turt.rt(90)
        spiral(turt, length - 5)


def nextSize(currSize):
    """Takes in the current straight-line length, and computes
    and returns the length of the isosceles triangle’s side. """
    hDist = (currSize / 2)
    vDist = hDist * math.tan(math.radians(45))
    hypot = math.sqrt(vDist ** 2 + hDist ** 2)
    return hypot

def levyC(turt, size, level):
    # fixme: EVERYTHING IS WRONG
    turt.lt(90)
    if level < 1:
        pass
    elif level == 1:
        turt.fd(size)
    elif level > 1:
        size2 = nextSize(size)
        accum = level
        for i in range(level):
            turt.lt(45)
            turt.fd(size2)
            turt.rt(90)
            turt.fd(size2)
            accum = accum - 1
            levyC(turt, size, accum)



def drawspiral():
    bob.penup()
    bob.goto(-300, 300)
    bob.pendown()
    spiral(bob, 600)
    sc.exitonclick()


def drawlevyC():
    levyC(bob, 100, 4)
    sc.exitonclick()

drawspiral()
drawlevyC()

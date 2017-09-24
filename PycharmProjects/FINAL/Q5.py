import turtle


# Your job in this question is to write a function named
# drawTriangles. The drawTrianges function draws a series
# of equilateral triangles, each one next to the other.
# The drawn squares start with 10 pixels to a side, and
# get bigger by 10 until they reach the input max size,
# after which they get smaller until they reach 10 again.
# The function has two parameters, a trutle object (which
# will be used to draw the squares) and a maximum size
# object (which should be a multiple of 10). This function
# does not need to return anything. See the included
# example output for more information.


def drawTrainages(turt, max):
    dist = 10
    while dist < max:
        for i in range(3):
            turt.fd(dist)
            turt.lt(120)
        turt.fd(dist)
        dist = dist + 10
    while dist >= 10:
        for i in range(3):
            turt.fd(dist)
            turt.lt(120)
        turt.fd(dist)
        dist = dist - 10




sc = turtle.Screen()
tur = turtle.Turtle()
drawTrainages(tur, 50)
sc.exitonclick()
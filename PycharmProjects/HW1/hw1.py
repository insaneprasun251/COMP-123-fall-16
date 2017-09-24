#COMP 123-04 HW 1
#,richard_graham>


#PART ONE
width = 75
height = 125

area = width*height

print(area)

#PART TWO
width = int(input("Enter a width"))
height = int(input("Enter a height"))

area2 = width*height

print(area2)

#PART THREE
import turtle

bob = turtle.Turtle()
win = turtle.Screen()

bob.color('red')
bob.down()

for i in range(2):
    bob.forward(width)
    bob.right(90)
    bob.forward(height)
    bob.right(90)

win.exitonclick()
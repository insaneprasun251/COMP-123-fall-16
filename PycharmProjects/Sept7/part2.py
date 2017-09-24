import turtle

window = turtle.Screen()
foo = turtle.Turtle()

bar = turtle.Turtle()

foo.color("pink")
foo.shape("circle")

bar.color("light green")
bar.shape("turtle")

bar.penup()
bar.goto(-400, 0)
bar.pendown()

for i in range(5):          #same loop for both turtles' stars
    foo.forward(400)
    foo.right(144)
    bar.forward(250)
    bar.left(144)

window.exitonclick()
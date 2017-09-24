import turtle

window = turtle.Screen()
bob = turtle.Turtle()

window.bgcolor("lavender")
bob.color("blue")
bob.forward(50)                 #makes a line left-right
bob.left(45)                    #45deg angle
bob.forward(50)                 #other side of the angle

window.exitonclick()

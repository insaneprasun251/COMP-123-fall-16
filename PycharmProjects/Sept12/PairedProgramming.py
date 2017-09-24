#Richard Graham
#Annastazia Harriott

import math

conversion = math.radians(1)


print(math.sin(30*conversion))

for i in range(5):
    print(i)
    print(math.sin(i*conversion))

for i in range(91):
    print(i, math.sin(i*conversion))

import turtle

Foo = turtle.Turtle()
Foo.shape("turtle")
Foo.color("blue")
window = turtle.Screen()

turtle.setworldcoordinates(0, -1, 360,1)
#This looks different!

Zozobra = turtle.Turtle()
Zozobra.color("purple")

yeti = turtle.Turtle()
yeti.left(90)
yeti.fd(1)
yeti.rt(90)
yeti.fd(5)
yeti.bk(5)
yeti.rt(90)
yeti.fd(1)
yeti.left(90)
yeti.fd(5)
yeti.bk(5)
yeti.rt(90)
yeti.fd(1)
yeti.lt(90)
yeti.fd(5)


for i in range(5):
    Zozobra.forward(90)
    Zozobra.left(90)
    Zozobra.fd(0.05)
    Zozobra.left(180)
    Zozobra.fd(0.1)
    Zozobra.left(180)
    Zozobra.fd(0.05)
    Zozobra.right(90)

#Foo.goto(70,80)

for i in range(361):
    Foo.goto(i, math.sin(i*conversion))

window.exitonclick()

#No, it looks like a line.




#PART ONE


4+9         #13 int
4+9.0       #13.0 float
3.2-1.1     #2.1 float
3-1         #2 int
3-1.0       #2.0 float
4*5         #20 int
4*6.5       #26.0 float
25/3        #8.33333 float
25/3.0      #8.33333 float
25//3       #8 int
25.0//3.0   #8.0 float
25%3        #1 int
40%11.0     #7.0 float
3**2        #9 int
2.0**3      #8.0 float

#PART TWO

import turtle

window = turtle.Screen()
turt = turtle.Turtle()

turt.speed(0)

for i in range(1,1080):
    turt.forward(i//360)
    turt.left(1)


window.exitonclick()

#Prediction: a segmented spiral made with 1-degree angles, with each segment getting longer by 1/360th?
#Outcome: pretty much that

#Prediction pt 2: for i = [1,360], turtle will rotate without moving.
# for i = [360, 720], turtle will make a circle.
# for i > 720, turt will move outward in a spiral
#Outcome pt 2: for i>720, turt made a bigger circle!

#explanation: values between 360 and 720 return a value of 1 on integer division. values between 720 and 1080 simply return 2.
#turt is making polygons by turning 1 degree at each vertex and making segments with lengths of 0, 1, and 2, respectively.

#PART THREE

len(longstr)                #longstr is also not yet defined in code. should return 7 if properly set up
'kits' in longstr           #again missing quotes. Would return False
print(longstr[36:39])       #values are longer than length of string

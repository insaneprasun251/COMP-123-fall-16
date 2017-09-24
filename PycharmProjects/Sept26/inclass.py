# Part 1

x = 25
y = 30
s = 'boolean'

print(x <= y)              #True
print(x + 5 > y)           #False
print(x % 2 == 0)          #False
print(s > 'bodwaddle')     #True
print(len(s) ==7)          #True
print('e' in s)            #True
print('c' in s)            #False
print('boo' in s)          #True
print(True == False)       #False
print(False == False)      #True
print(7 != 7)              #False

# ======================================
print()
# ======================================

# Part 2


def isSmall(x):
    return x <= 10

print(isSmall(8))

# ======================================
print()
# ======================================

# Part 3


def isEven(x):
    return x % 2 == 0

print(isEven(100))

# ======================================
print()
# ======================================

# Part 4

print((x % 5 == 0) and (y % 5 == 0))        # True
print((s[0] == 'b') or (len(s) >= 10))      # True
print('l' not in s)                         # False
print(not (s[1] == 'a'))                    # True
nums = [15, 20, 25, 30]
print((x in nums) and not (y in nums))      # False
print((x >= 15) and (x <= 50))              # True

# ======================================
print()
# ======================================

# Part 5


def bigEven(x):
    return isEven(x) and not isSmall(x)

print(bigEven(20))


# ======================================
print()
# ======================================

# Part 6

x = 7
y = 7

if x > y:
    print(x, y)
elif y > x:
    print(y, x)
else:
    print(x)

# prints the greater of the two numbers followed by the lesser, or the value of both if they're equal

# ======================================
print()
# ======================================

# Part 7


def evaluate(x):
    if bigEven(x):
        print("wow I love this number. It's so big!")
    elif not isSmall(x):
        print("It's pretty big, but it's not the best")
    else:
        print("it's a pretty small number")

evaluate(9)


# ======================================
print()
# ======================================

# Part 8

def min3(x, y, z):
    if x <= y and x <=z:
        print(x)
    elif y <= x and y <=z:
        print(y)
    else:
        print(z)

min3(70, 54, 200)

# ======================================
print()
# ======================================

# Part 9

import turtle


def doMove(teleT, move):
    if move == "f":
        teleT.fd(15)
    elif move == "b":
        teleT.bk(15)
    elif move == "r":
        teleT.rt(90)
    elif move == "l":
        teleT.lt(90)
    else:
        print("invalid input")


def teleTurtle(n):
    win = turtle.Screen()
    teleT = turtle.Turtle()
    for i in range(n):
        move = input("Enter next move: ")
        doMove(teleT, move)
    win.exitonclick()


teleTurtle(5)


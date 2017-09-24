import turtle

wind = turtle.Screen()
turt1 = turtle.Turtle()
turt1.up()
turt1.goto(100,100)
turt1.down()

turt2 = turtle.Turtle()
turt2.up()
turt2.goto(-100, -100)
turt2.down()

turt3 = turt1       # gives us another name to refer to turt1/creates an Alias

# this line of code creates a new turtle that is a 'copy' of a previous turtle.
turt4 = turt2.clone()   # creates a totally new turtle at the same position as turt2.

for i in range(4):
    turt1.forward(100)  # turt1/3 goes forward
    turt3.left(90)      # turt1/3 turns left
    turt2.backward(100) # turt 2 moves
    turt4.right(90)     # turt 4 turns w/out moving

wind.exitonclick()

def addN(z, n):
    z.insert(0,str(n))

x=[]                    # x = []
y=x                     # y = []
x.insert(0, "apple")    # x = ["apple"]
z=y+["pies"]            # z = ["apple", "pies"]
addN(y, 10)             # x, y = [10, "apple"]
z.append("sound good")  # ["apple", "pies", "sound good"]
z[0] = "lemon"          # ["lemon", "pies", "sound good"]
w=z[:]                  # w = ["lemon", "pies", "sound good"]
print (x)               # ["10", "apples]
print (y)               # ["10", "apples]
print (z)               # ["lemon", "pies", "sound good"]
print (w)               # ["lemon", "pies", "sound good"]
print(x == y)           # True
print(x is y)           # True
print(w == z)           # True
print(w is z)           # False


def doubleList(inList):
    outlist = [elem * 2 for elem in inList]
    return outlist


def doubleListInPlace(inList):
    for elem in range(len(inList)):
        inList[elem] = elem * 2

testList = [1, 2, 5]

print(doubleList(testList))
print(doubleListInPlace(testList))
print(testList)

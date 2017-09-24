###Question One

numberOfPacks = 3
eggsPerPack = 13
eggsPerBatchOfCookies = 2

numberOfEggs = numberOfPacks*eggsPerPack
numberOfBatches = numberOfEggs//eggsPerBatchOfCookies

print(numberOfBatches)


###Question Two

import turtle

wind = turtle.Screen()
spiro = turtle.Turtle()
spiro.speed(0) #the fastest speed achievable by turtle-kind

userDist = input("What distance?")
userTurn = input("What angle?")

spiralDist = float(userDist)
spiralTurn = float(userTurn)

for i in range(100):
    spiro.fd(spiralDist)
    spiro.lt(spiralTurn)

wind.exitonclick()

###Part Three

for i in range(1, 102,2):
    print(i*i)

print("done")
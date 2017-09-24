# Part 1

import math


def someFunc(lst):
    variable = "blank 1"
    for elem in lst:
        variable = "blank 2"
    return variable

# 1. F
# 2. E
# 3. Q
# 4. G
# 5. O


# Part 2

def countUserVowels():
    inStr = input("type something")
    print("number of a", inStr.count("a"))
    print("number of e", inStr.count("e"))
    print("number of i", inStr.count("i"))
    print("number of o", inStr.count("o"))
    print("number of u", inStr.count("u"))

countUserVowels()

def toLengthList(stringList):
    for i in range(len(stringList)):
        stringList[i] = len(stringList[i])


lst = ["I", "am", "a", 'very', 'happy', 'person']

toLengthList(lst)
print(lst)
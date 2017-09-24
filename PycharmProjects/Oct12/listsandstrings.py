def firstN(n, inList):
    outList = []
    if n > len(inList):
        return inList
    else:
        for i in range(0, n):
            outList.append(inList[i])
        return outList

list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 789]
print(firstN(5, list))


def firstNStr(n, inStr):
    outStr = ""
    if n > len(inStr):
        return inStr
    else:
        for i in range(0, n):
            outStr = outStr + inStr[i]
        return outStr

str = "Pineapples are in my head"
print(firstNStr(17, str))


def divisibleList(length, base):
    outlist = []
    for i in range(1, length + 1):
        if i % base == 0:
            outlist.append(True)
        else:
            outlist.append(False)
    return outlist

print(divisibleList(10, 3))


def multiplyByIndex(inList):
    for i in range(len(inList)):
        inList[i] = inList[i] * i
    return inList

print(multiplyByIndex(list))


def multiplyByIndexPure(inList):
    outList = []
    for i in range(len(inList)):
        outList.append(inList[i] * i)
    return outList

print(multiplyByIndexPure(list))


def onlyEven(inList):
    newList = []
    for elem in inList:
        if elem % 2 == 0:
            newList.append(elem)
        else:
            pass
    return newList

print(onlyEven(list))



strA = "I bought a scarf today."
lstA = [1, 2, 3, 4, 5, 4, 3, 2, 1]

print(strA[15])
print(lstA[4])

print(strA[17:20])
print(lstA[3:6])

strB = "Martha told me: " + strA
lstB = [-3, -2, -1, 0] + lstA

print(strB)
print(lstB)

print("asd" in strA)
print([4, 5, 4] in lstB)
print(4 in lstB)

# in doesn't work with searching lists in lists--because lists can be elements in lists, it only allows
# of a single element of the list.

print(min(strA), max(strA))
print(min(lstB), max(lstB))

print(strB)
print(strB.index("toda"))

print(lstB.index(5))

# index of [0, 1, 2] is not possible--the index method only finds individual elements of lists

if len(lstB) >= len(strB):
    print(lstB)
else:
    print(strB)

strC = strB.upper()
print(strC)

print(sum(lstB))


def myLength(inList):
    length = 0
    for i in inList:
        length = length + 1
    return length

print(myLength(lstB))

def mySum(inList):
    sum = 0
    for i in inList:
        sum = sum + i
    return sum

print(mySum(lstA))

def numsToString(inList):
    outStr = ""
    for element in inList:
        outStr = outStr + str(element)
    return outStr

print(numsToString(lstB))

def stringOfNumsToList(inStr):
    outLst = []
    for nums in inStr:
        outLst.append(int(nums))
    return outLst

print(stringOfNumsToList("1286047"))


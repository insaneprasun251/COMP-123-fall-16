# Part One

strA = "I bought a scarf today"

print(strA[12:15])

strB = "Marta told me: " + strA

print(strB)

print('today' in strA)

strC = strB.upper()

print(strA.find('arf'))

if strA >= "What did you say?":
    shortString = "What did you say?"
elif strA <= "What did you say?":
    shortString = strA
else:
    pass

# Part Two


def shout(inStr):
    newStr = inStr.upper()
    return newStr

# Part Three


def areYouTalkingAboutMe(inStr):
    return "Richard" in inStr

print(areYouTalkingAboutMe("Richard is cool"))

# Part Four


def countE(inStr):
    numTimes = inStr.count("E") + inStr.count("e")
    return numTimes

print(countE("big yellow Elephants"))


def countE2(inStr):
    count = 0
    strIndex = 0
    while strIndex <= len(inStr):
        if inStr[strIndex] == "e" or inStr[strIndex] == "E":
            count = count + 1
        else:
            strIndex = strIndex + 1
    return count

print(countE2("big yellow Elephants"))

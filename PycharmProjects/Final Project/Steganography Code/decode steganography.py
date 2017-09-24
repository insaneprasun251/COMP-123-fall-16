from imageToolsTools import *


def modulusDecode(pic):
    letterList = []

    for x in range(getWidth(pic)):
        for y in range(getHeight(pic)):
            pix = getPixel(pic, x, y)
            r = getRed(pix)
            g = getGreen(pix)
            b = getBlue(pix)
            a = getAlpha(pix)

            letter = ""

            color = [r, g, b, a]

            for element in color:
                remainder = element % 4
                if remainder == 0:
                    letter = letter + "00"
                if remainder == 1:
                    letter = letter + "01"
                if remainder == 2:
                    letter = letter + "10"
                if remainder == 3:
                    letter = letter + "11"

            letterList.append(letter)
    return letterList


def binaryToString(binaryList):
    output = ""
    for element in binaryList:
        ASCII = int(element, 2)
        char = chr(ASCII)
        output = output + char
    return output


def main():
    pictodecode = makePicture(pickAFile())
    rawtext = binaryToString(modulusDecode(pictodecode))
    cleantext = rawtext.split("\0\0\0\0")
    print(cleantext[0])

main()

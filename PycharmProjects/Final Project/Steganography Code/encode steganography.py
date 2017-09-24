# Steganography encoding script
#
# this script uses imageTools to encode an input text into an image that is nearly indistinguishable from the original.
# Because of the name of this technique, we chose to use a stegosaurus to steganographically encode.
#
# Raney Bice, Richard Graham, Maggie Hohenstein
# COMP 123-03, 123-04
# Daniel Kluver

from imageToolsTools import *


def stringtoASCII(instr):
    """convert the input text string to a list of ASCII code numbers"""
    outlist = [ord(c) for c in instr]
    return outlist


def ASCIItobinary(inlist):
    """convert a list of 8-bit numbers into a list of 8-digit binary string elements"""
    outlist = []
    for elem in inlist:
        binelem = format(elem, "08b")
        outlist.append(binelem)
    return outlist


def prepareimage():
    """use the imageTools library to open a picture and prepare it as a picture object for pixel manipulation"""
    stan = makePicture("./stan the stegosaurus.tiff")
    return stan


def charactertest(string, heightpix, widthpix):
    """Tester function: if the input string is longer than can be encoded in the picture, return False"""
    if len(string) > heightpix * widthpix:
        return True
    else:
        return False


def getTwo(inList, position):
    """input the list of binary strings representing characters to encode, as well as the desired position in the list,
    i.e. the letter to be encoded. return the binary string in question as a list of 4 2-digit string elements"""
    letter = inList[position]
    letterList = []

    for i in range(0, 7, 2):
        add = str(letter[i:i+2])
        letterList.append(add)

    return letterList


def modulusarithmetic(pixval, modulus):
    """take an input color value and change it to the nearest value with the desired remainder when divided by 4"""
    remainder = pixval % 4
    if remainder != modulus:
        pixval = pixval + (modulus - remainder)
    return pixval


def findmodulus(inchar):
    """determine the desired modulus for the pixel values depending on values of input binaries"""
    mod = 10000
    if inchar == "00":
        mod = 0
    elif inchar == "01":
        mod = 1
    elif inchar == "10":
        mod = 2
    elif inchar == "11":
        mod = 3
    return mod


def getpix(pic, words):

    lengthtracker = len(words)

    numloops = 0
    for x in range(getWidth(pic)):
        for y in range(getHeight(pic)):
            if numloops >= lengthtracker:
                break

            pix = getPixel(pic, x, y)

            r = getRed(pix)
            g = getGreen(pix)
            b = getBlue(pix)
            a = getAlpha(pix)

            colorlist = [r, g, b, a]

            charactertoencode = getTwo(words, numloops)

            encoderloopcount = 0

            for elem in charactertoencode:
                mod = findmodulus(elem)

                colorchannel = colorlist[encoderloopcount]

                newval = modulusarithmetic(colorchannel, mod)

                if encoderloopcount == 0:
                    setRed(pix, newval)
                elif encoderloopcount == 1:
                    setGreen(pix, newval)
                elif encoderloopcount == 2:
                    setBlue(pix, newval)
                elif encoderloopcount == 3:
                    setAlpha(pix, newval)

                encoderloopcount = encoderloopcount + 1

            numloops = numloops + 1

    return pic


def main():
    pic = prepareimage()
    w = getWidth(pic)
    h = getHeight(pic)

    secret = input("What do you want to encode? ")
    newsecret = secret.replace("\0", "\n") + "\0\0\0\0"

    if charactertest(secret, h, w):
        print("ERROR: Input string is too long, please try a different string")
        quit()

    secret2 = stringtoASCII(newsecret)
    secret3 = ASCIItobinary(secret2)

    resultstan = getpix(pic, secret3)

    filename = "stan the encoded stegosaurus.tif"

    savePicture(resultstan, filename)

    print("Encoded image has been saved to: ", filename)

main()

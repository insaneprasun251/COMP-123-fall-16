# Nov 12 drafts for ASCII conversion
# Richard Graham
# ===================================

import string

from imageToolsTools import *


def stringtoASCII(instr):
    """converts the input text string to a list of ASCII code numbers"""
    outlist = [ord(c) for c in instr]
    return outlist


def ASCIItobinary(inlist):
    """converts a list of 8-bit numbers into a list of 8-digit binary string elements"""
    outlist = []
    for elem in inlist:
        binelem = format(elem, "08b")
        outlist.append(binelem)
    return outlist


def prepareimage():
    """uses the imageTools library to open a picture and prepare it as an object for pixel manipulation"""
    stan = makePicture("./stan the stegosaurus.png")
    return stan

# FIXME: In Progress - RG 11/30 @5:00PM
# FIXME: there are so many problems here I'm v confused I'm sorry

# okay so I think the approach here is to make a couple functions out of this instead?
# i.e. let's get states of each segment of each binary element (if the first 2 digits are 00, 01, 10, or 11
# or something) and then hella if statements to manipulate the pixels based on that..?
#

# def badsteganography(binary, pic=prepareimage()):
#     allpix = getPixels(pic)
#     w = getWidth(pic)
#     h = getHeight(pic)
#     for x in range(0, w, 8):
#         for y in range(0, h, 8):
#             if binary[0][0:1] == "00":
#                 return "step 1 works"
#             elif binary[0][2:3] == "00":
#                 return "step 2 works"

# def preparepixels(pic=prepareimage()):
#     """takes in a picture object and returns pixel data as lists of binaries for manipulation"""
#     # FIXME: RG: this returns enormous lists of all pixel data - should this be broken down into lists by row or column
#     # fixme: of pixels? e.g. for x in width of pic: return rgb data at one y value, then make a new list for the next
#     # fixme: y value?
#     redlist = []
#     greenlist = []
#     bluelist = []
#     for pix in getPixels(pic):
#         tempr = getRed(pix)
#         redlist.append(tempr)
#
#         tempg = getGreen(pix)
#         greenlist.append(tempg)
#
#         tempb = getBlue(pix)
#         bluelist.append(tempb)
#     return redlist, greenlist, bluelist


def steg2(binary, pic=prepareimage()):
    # Fixme: RG: format pixel data in a separate function, then change steg2 to simply take 2 input lists and manipulate
    # fixme: RG: them accordingly
    listpos = 0
    for pix in getPixels(pic):
        r1 = getRed(pix)
        r2 = bin(r1)                    # format better--bin() doesn't do what we want
        r3 = r2 + binary[listpos]       # string concatenation vs binary addition???
        listpos = listpos + 1
        return r3


def runtests():
    """TEMP functions for testing the program piecewise"""
    text = string.ascii_letters
    # text = input("enter a string")

    print(text)

    ASCIIlist = stringtoASCII(text)
    print(stringtoASCII(text))

    binary = ASCIItobinary(ASCIIlist)
    print(binary)

    stanley = prepareimage()
    show(stanley)
    wait(stanley)
    # Stanley appears in background, process will not end unless he's clicked on. this is a "feature" not a bug.

    print(steg2(binary, stanley))Î


# def testpics():
#     stan = prepareimage()
#     r, g, b = preparepixels(stan)
#     w = getWidth(stan)
#     h = getHeight(stan)
#     newpic = makeEmptyPicture(w,h)
#     for x in range(w):
#         for y in range(h):
#             pix = getPixel(newpic, x, y)
#             setRed(pix, r[x])
#             setGreen(pix, g[x])
#             setBlue(pix, b[x])
#     show(newpic)
#     wait(newpic)
#
#     print("check picture")

# Maggie added some shit and didn't know where to put it so here

from imageTools import *
from imageToolsTools import *


def getTwo(inList,position):
    letter = inList[position]
    letterList = []
    for i in range(0,7,2):
        add = str(letter[i:i+2])
        letterList.append(add)
    return letterList

listt = ["00001011", "11010101", "11101101", "00101101", "10110110"]

print(getTwo(listt,0))


def changePix(letterList,pix):
    r = getRed(pix)
    b = getBlue(pix)
    g = getGreen(pix)
    a = getAlpha(pix)

    if letterList[0] == "00":
        setRed(pix, r)
    elif letterList[0] == "01":
        setRed(pix, r+1)
    elif letterList[0] == "10":
        setRed(pix, r+2)
    elif letterList[0] == "11":
        setRed(pix, r-1)

    if letterList[1] == "00":
        setBlue(pix, b)
    elif letterList[1] == "01":
        setBlue(pix, b+1)
    elif letterList[1] == "10":
        setBlue(pix, b+2)
    elif letterList[1] == "11":
        setBlue(pix, b-1)

    if letterList[2] == "00":
        setGreen(pix, g)
    elif letterList[2] == "01":
        setGreen(pix, g+1)
    elif letterList[2] == "10":
        setGreen(pix, g+2)
    elif letterList[2] == "11":
        setGreen(pix, g-1)

    if letterList[3] == "00":
        setAlpha(pix, a)
    elif letterList[3] == "01":
        setAlpha(pix, a+1)
    elif letterList[3] == "10":
        setAlpha(pix, a+2)
    elif letterList[3] == "11":
        setAlpha(pix, a-1)


# testpics()

# runtests()

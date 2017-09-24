from imageTools import *
from imageToolsTools import *


def getTwo(inList,position):
    letter = inList[position]
    letterList = []
    for i in range(0,7,2):
        add = str(letter[i:i+2])
        letterList.append(add)
    return letterList

listt = ["11111111","11010101","11101101","00101101","10110110"]


def changePix(letterList,picture,pixx,pixy):
    pix = getPixel(picture,pixx,pixy)
    r = getRed(pix)
    b = getBlue(pix)
    g = getGreen(pix)
    a = getAlpha(pix)

    # FIXME: I don't know how to do transparency, and we need to include way to code this
    # Richard added at the bottom!

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


letList = getTwo(listt,0)
pic = makeEmptyPicture(100,100)
show(pic)
wait(pic)
changePix(letList,pic,50,50)
show(pic)
wait(pic)
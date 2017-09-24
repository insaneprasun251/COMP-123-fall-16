from imageToolsTools import *

# pt 1: the code opens a picture, looks at all of its pixels, and for each one resets the red value to be
# the original red value times the 'factor' the user specifies.

# pt 2

def grayscale(pic):
    newPic = copyPicture(pic)
    for pixel in getPixels(newPic):
        r = getRed(pixel)
        g = getGreen(pixel)
        b = getBlue(pixel)
        lumin = (r + g + b) / 3
        setColor(pixel, makeColor(lumin, lumin, lumin))
    return newPic


def weightedScale(picture, redweight, greenweight, blueweight):
    newpic = copyPicture(picture)
    for pixel in getPixels(newpic):
        r = getRed(pixel)
        g = getGreen(pixel)
        b = getBlue(pixel)
        lumin = (r * redweight + g * greenweight + b * blueweight)
        setColor(pixel, makeColor(lumin, lumin, lumin))
    return newpic


def removeblue(pic):
    newpic = copyPicture(pic)
    for pixel in getPixels(newpic):
        setBlue(pixel, 0)
    return newpic


def fixgreen(pic, grnval):
    newpic = copyPicture(pic)
    for pixel in getPixels(newpic):
        setGreen(pixel, grnval)
    return newpic



pic1 = makePicture("../Oct24/MediaSources/flowers-on-blue.jpg")
greybigben = grayscale(pic1)
weightb = weightedScale(pic1, 0.2126, 0.7152, 0.0722)
noblue = removeblue(pic1)
fixgrn = fixgreen(pic1, 127)
show(greybigben)
wait(greybigben)
show(weightb)
wait(weightb)
show(noblue)
wait(noblue)
show(fixgrn)
wait(fixgrn)

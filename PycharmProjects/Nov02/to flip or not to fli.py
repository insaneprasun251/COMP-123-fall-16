import math
from imageTools import *
from imageToolsTools import *


def mirrorimage(sourcepicture):
    targetpic = duplicatePicture(sourcepicture)
    for sourcex in range(0, math.floor((getWidth(sourcepicture) - 1) / 2) + 1):
        for sourcey in range(getHeight(sourcepicture)):
            targety = sourcey
            targetx = (getWidth(sourcepicture) - 1) - sourcex
            sourcepix = getPixel(sourcepicture, sourcex, sourcey)
            targetpix = getPixel(targetpic, targetx, targety)
            col = getRGB(sourcepix)
            setRGB(targetpix, col)

    return targetpic

# picture = makePicture(pickAFile())
# mirroredpicture = mirrorimage(picture)
# show(mirroredpicture)
# wait(mirroredpicture)


def copycolor(inpx, outpx):
    rgb = getRGB(inpx)
    setRGB(outpx, rgb)
    return outpx

def rotateright(inpic):
    inw = getWidth(inpic)
    inh = getHeight(inpic)
    outpic = makeEmptyPicture(inh, inw)
    for sourcex in range(inw):
        targy = sourcex
        for sourcey in range(inh):
            targx = inh - sourcey - 1
            inpx = getPixel(inpic, sourcex, sourcey)
            outpx = getPixel(outpic, targx, targy)
            copycolor(inpx, outpx)
    return outpic


# rightpic = rotateright(picture)
# show(rightpic)
# wait(rightpic)


def copyDemo(smallPic, bigPic):
    targetX = 25
    for sourceX in range(getWidth(smallPic)):
        targetY = 25
        for sourceY in range(getHeight(smallPic)):
            srcPixel = getPixel(smallPic, sourceX, sourceY)
            tgtPixel = getPixel(bigPic, targetX, targetY)
            setColor(tgtPixel, getColor(srcPixel))
            targetY = targetY + 1
        targetX = targetX + 1
        return bigPic


# bigpic = makePicture(pickAFile())
# lilpic = makePicture(pickAFile())
#
# newpic = copyDemo(lilpic, bigpic)
# show(newpic)
# wait(newpic)


def scaledown(inpic):
    w = getWidth(inpic)
    h = getHeight(inpic)
    outpic = makeEmptyPicture(w, h)

    for x in range(w / 2):
        for y in range(h / 2):
            oldpix = getPixel(inpic, 2 // x, 2 // y)
            newpix = getPixel(outpic, x, y)
            setColor(newpix, getColor(oldpix))
    return outpic

pic = makePicture(pickAFile())
newpic = scaledown(pic)
show(pic)
wait(pic)


from imageTools import *
from imageToolsTools import *


def backsubstitute(frontpic, backpic, newback):
    h = getHeight(frontpic)
    w = getWidth(frontpic)
    outpic = makeEmptyPicture(w, h)

    for x in range(w):
        for y in range(h):
            frontpix = getPixel(frontpic, x, y)
            backpix = getPixel(backpic, x, y)
            newpix = getPixel(newback, x, y)
            outpix = getPixel(outpic, x, y)

            frontcol = getColor(frontpix)
            backcol = getColor(backpix)
            newcol = getColor(newpix)

            colparam = distance(frontcol, backcol)
            if colparam <= 125:
                setColor(outpix, newcol)
            else:
                setColor(outpix, frontcol)
    return outpic



def pixelisbackground(pixel):
    col = getColor(pixel)
    chroma = makeColor(0, 160, 80)
    colparam = distance(col, chroma)
    if colparam <75:
        return True
    else:
        return False


def chromakey(pic, newback):
    h = getHeight(pic)
    w = getWidth(pic)
    outpic = makeEmptyPicture(w,h)

    for x in range(w):
        for y in range(h):
            frontpix = getPixel(pic, x, y)
            newpix = getPixel(outpic, x, y)
            backpix = getPixel(newback, x, y)

            if pixelisbackground(frontpix):
                setColor(newpix, getColor(backpix))
            else:
                setColor(newpix, getColor(frontpix))
    return outpic

pic1 = makePicture("/Users/richardgraham/Google Drive/COMP 123-04/PycharmProjects/Nov09/comp 123-4 green screen photos/IMG_0802.jpg")
pic2 = makePicture("/Users/richardgraham/Google Drive/COMP 123-04/PycharmProjects/Nov09/comp 123-4 green screen photos/IMG_0780.jpg")
pic3 = makePicture("/Users/richardgraham/Google Drive/COMP 123-04/PycharmProjects/Nov09/comp 123-4 green screen photos/BackgroundPics/chicago.jpg")


def main():
    subst = backsubstitute(pic1, pic2, pic3)
    show(subst)
    wait(subst)

    chrom = chromakey(pic1, pic3)
    show(chrom)
    wait(chrom)

main()
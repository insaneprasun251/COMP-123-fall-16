# QUIZ 5
# Richard Graham, Nov 11

from imageTools import *
from imageToolsTools import *


def blackwhite(inpic, threshold):
    """returns a copy of the input image with a two-tone threshold effect, where pixels above the threshold for luminance
    are white and pixels below it are black"""
    w = getWidth(inpic)
    h = getHeight(inpic)
    outpic = makeEmptyPicture(w, h)

    for x in range(w):
        for y in range(h):
            inpix = getPixel(inpic, x, y)
            outpix = getPixel(outpic, x, y)

            r, g, b = getRGB(inpix)
            luma = ((r + g + b) / 3)
            if luma <= threshold:
                setColor(outpix, black)
            else:
                setColor(outpix, white)
    return outpic


def gradualblend(inpic1, inpic2):
    """blends two pictures in a horizontal gradient"""
    w = getWidth(inpic1)
    h = getHeight(inpic1)
    outpic = makeEmptyPicture(w, h)

    for x in range(w):
        for y in range(h):
            inpix1 = getPixel(inpic1, x, y)
            inpix2 = getPixel(inpic2, x, y)
            outpix = getPixel(outpic, x, y)

            r1, g1, b1 = getRGB(inpix1)
            r2, g2, b2 = getRGB(inpix2)

            weight1 = x / w
            weight2 = 1 - weight1

            setRed(outpix, (r1 * weight1 + r2 * weight2))
            setGreen(outpix, (g1 * weight1 + g2 * weight2))
            setBlue(outpix, (b1 * weight1 + b2 * weight2))

    return outpic


def main():
    pic1 = makePicture("/Users/richardgraham/Google Drive/COMP 123-04/PycharmProjects/Oct24/MediaSources/red.JPG")
    pic2 = makePicture("/Users/richardgraham/Google Drive/COMP 123-04/PycharmProjects/Oct24/MediaSources/gorge.JPG")
    pic3 = makePicture("/Users/richardgraham/Google Drive/COMP 123-04/PycharmProjects/Oct24/MediaSources/graves.JPG")

    result1 = blackwhite(pic1, 100)
    show(result1)
    wait(result1)

    result2 = blackwhite(pic1, 205)
    show(result2)
    wait(result2)

    result3 = gradualblend(pic2, pic3)
    show(result3)
    wait(result3)

main()

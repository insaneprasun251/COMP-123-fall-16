from imageTools import *
from imageToolsTools import *

def simpleblend(inpic1, inpic2):
    h = getHeight(inpic1)
    w = getWidth(inpic1)
    outpic = makeEmptyPicture(w, h)
    for y in range(h):
        for x in range(w):
            inpix1 = getPixel(inpic1, x, y)
            inpix2 = getPixel(inpic2, x, y)

            r1, g1, b1 = getRGB(inpix1)
            r2, g2, b2 = getRGB(inpix2)

            outpix = getPixel(outpic, x, y)

            setRed(outpix, (r1 + r2) / 2)
            setGreen(outpix, (g1 + g2) / 2)
            setBlue(outpix, (b1 + b2) / 2)


    return outpic


def blendpictures(inpic1, inpic2):
    h1 = getHeight(inpic1)
    w1 = getWidth(inpic1)

    h2 = getHeight(inpic2)
    w2 = getWidth(inpic2)

    h3 = min(h1, h2)
    w3 = min(w1, w2)

    outpic = makeEmptyPicture(w3, h3)
    for y in range(h3):
        for x in range(w3):
            inpix1 = getPixel(inpic1, x, y)
            inpix2 = getPixel(inpic2, x, y)

            r1, g1, b1 = getRGB(inpix1)
            r2, g2, b2 = getRGB(inpix2)

            outpix = getPixel(outpic, x, y)

            setRed(outpix, (r1 + r2) / 2)
            setGreen(outpix, (g1 + g2) / 2)
            setBlue(outpix, (b1 + b2) / 2)

    return outpic


def weightedblend(inpic1, inpic2, weight1):

    weight2 = 1.0 - weight1

    h1 = getHeight(inpic1)
    w1 = getWidth(inpic1)

    h2 = getHeight(inpic2)
    w2 = getWidth(inpic2)

    h3 = min(h1, h2)
    w3 = min(w1, w2)

    outpic = makeEmptyPicture(w3, h3)
    for y in range(h3):
        for x in range(w3):
            inpix1 = getPixel(inpic1, x, y)
            inpix2 = getPixel(inpic2, x, y)

            r1, g1, b1 = getRGB(inpix1)
            r2, g2, b2 = getRGB(inpix2)

            outpix = getPixel(outpic, x, y)

            setRed(outpix, (r1 * weight1 + r2 * weight2))
            setGreen(outpix, (g1 * weight1 + g2 + weight2))
            setBlue(outpix, (b1 * weight1 + b2 * weight2))

    return outpic



pic1 = makePicture(pickAFile())
pic2 = makePicture(pickAFile())

# pic3 = simpleblend(pic1, pic2)
# show(pic3)
# wait(pic3)

pic4 = weightedblend(pic1, pic2, 0.25)
show(pic4)
wait(pic4)
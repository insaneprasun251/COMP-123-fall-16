from imageTools import *
from imageToolsTools import *
paf = "/Users/richardgraham/Google Drive/COMP 123-04/PycharmProjects/Oct24/MediaSources/arch.jpg"
picture = makePicture(paf)


def makeMoreGray(pic):
    for x in range(getWidth(pic)):
        for y in range (getHeight(pic)):
            pixel = getPixel(pic, x, y)
            r = getRed(pixel)
            g = getGreen(pixel)
            b = getBlue(pixel)

            setRed(pixel, ((3*r)+g+b)//5)
            setGreen(pixel, (r+(3*g)+b)//5)
            setBlue(pixel, (r+g+(3*b))//5)


show(picture)
wait(picture)
makeMoreGray(picture)
show(picture)
wait(picture)
makeMoreGray(picture)
show(picture)
wait(picture)


def lightenRegion(pic, ulx, uly, lrx, lry):
    outpic = copyPicture(pic)
    for x in range(ulx, lrx + 1):
        for y in range(uly, lry + 1):
            pixel = getPixel((outpic, x, y))
            r, g, b = getRGB(pixel)
            rgb = r * 2, g * 2, b * 2
            setRGB(pixel, rgb)

lightenRegion(picture, 12, 12, 100, 100)
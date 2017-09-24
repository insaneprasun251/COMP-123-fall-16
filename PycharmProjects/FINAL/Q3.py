from imageTools import *
import time

# In this question you will write a function named
# mergeRGB that takes three images and returns a new
# image. The three images will be merged by taking the
# red chanel from the first image, the green chanel from
# the second image, and the blue chanel from the third
# image. This will result in a new image which will look
# pretty cool (in my opinion). The images may not be the
# same size so you should make your new image have the
# minimum width of the three images and the minimum
# height of the three images.


def mergeRGB(rImage, gImage, bImage):
    w1 = getWidth(rImage)
    w2 = getWidth(gImage)
    w3 = getWidth(bImage)
    outw = min(w1, w2, w3)

    h1 = getHeight(rImage)
    h2 = getHeight(gImage)
    h3 = getHeight(bImage)
    outh = min(h1, h2, h3)

    outpic = makeEmptyPicture(outw, outh)

    for x in range(outw):
        for y in range(outh):
            rpix = getPixel(rImage, x, y)
            gpix = getPixel(gImage, x, y)
            bpix = getPixel(bImage, x, y)
            newpix = getPixel(outpic, x, y)

            rval = getRed(rpix)
            gval = getGreen(gpix)
            bval = getBlue(bpix)

            (r, g, b) = rval, gval, bval

            setRGB(newpix, (r, g, b))

    return outpic


r = makePicture("blackcat.jpg")
g = makePicture("jungle2.jpg")
b = makePicture("blueMotorcycle.jpg")
ni = mergeRGB(r, g, b)
show(ni)
time.sleep(15)
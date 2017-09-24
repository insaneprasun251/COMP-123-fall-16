from imageToolsTools import *

pic1 = makePicture("./stan the stegosaurus.tiff")
pic2 = makePicture("12345.tif")

w = getWidth(pic1)
h = getHeight(pic1)

for y in range(7):
    pix1 = getPixel(pic1, 0, y)
    pix2 = getPixel(pic2, 0, y)
    print(pix1)
    print(pix2)



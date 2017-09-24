from imageTools import *
import time

pic1 = makePicture("MediaSources/butterfly2.jpg")
pic2 = makePicture("MediaSources/horse.jpg")
pic3 = makePicture("MediaSources/redDoor.jpg")

show(pic1)
show(pic2)
show(pic3)

pic2w = getWidth(pic2)
pic2h = getHeight(pic2)

pic3pixel = getPixel(pic3, 25, 100)

print("pic2 is:", pic2w, "pixels wide and:", pic2h, "pixels high.")
print("pic3 is:", pic3pixel)


pixIt = getPixels(pic1)
pixList = list(pixIt)
print(pixList[0:3])
from imageTools import *
from imageToolsTools import *

# =======================================
# hw6Code.py
#
# This file contains code I've provided to you.  You may use this file
# to put your answers in, as well.
# =======================================
# Richard Graham
# COMP 123-04
# HW 6
# ---------------------------------------
# Question 1

# Put your definition of wallpaper here,  use the test function in hw6Tests.py to test it 


def pictowallpaper(inpic, outpic, xpos, ypos):
    """copies an input picture object to an output picture object at specified starting coordinates"""
    w = getWidth(inpic)
    h = getHeight(inpic)
    for x in range(w):
        for y in range(h):
            inpix = getPixel(inpic, x, y)
            outpix = getPixel(outpic, x + xpos, y + ypos)
            col = getColor(inpix)
            setColor(outpix, col)




def wallpaper(inpic, rows, columns):
    """repeats the input picture in a grid of specified dimensions to make a wallpaper
    that is returned as a new picture object"""
    w1 = getWidth(inpic)
    h1 = getHeight(inpic)
    w2 = w1 * columns
    h2 = h1 * rows
    outpic = makeEmptyPicture(w2, h2)
    for x in range(columns):
        for y in range(rows):
            pictowallpaper(inpic, outpic, x * w1, y * h1)
    return outpic

# ---------------------------------------
# Question 2

def rotateLeft(pic):
    """Takes in a picture object, and it creates a new picture object that has been rotated 90 degrees
    to the left (counter-clockwise) from the original.  It returns the new picture object."""
    newPic = makeEmptyPicture(getHeight(pic), getWidth(pic))
    for x in range(getWidth(newPic)):
        for y in range(getHeight(newPic)):
            newPix = getPixel(newPic, x, y)
            oldX = getWidth(pic) - y - 1
            oldY = x
            oldPix = getPixel(pic, oldX, oldY)
            setColor(newPix, getColor(oldPix))
        repaint(newPic)
    return newPic


# Put your definition of upsideDown here, and use the testing function in hw6Tests.py to test it


def upsideDown(pic):
    """takes in a picture object, and it creates a new picture object that has been rotated 180 degrees .
    the new picture object is returned."""
    newpic = makeEmptyPicture(getWidth(pic), getHeight(pic))
    for x in range(getWidth(pic)):
        for y in range(getHeight(pic)):
            newpix = getPixel(newpic, x, y)
            oldY = getHeight(pic) - y - 1
            oldX = getWidth(pic) - x - 1
            oldpix = getPixel(pic, oldX, oldY)
            setColor(newpix, getColor(oldpix))
    return newpic

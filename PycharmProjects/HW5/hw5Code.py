#  Homework 3 <Richard Graham>

from imageTools import *
import string


# Question 1
# put definition of encrypt here


def encrypt(filename1, filename2, cipher):
    """using the dictionary entered in cipher, the encrypt function writes file 1
    to file 2 as encrypted."""
    filein = open(filename1, "r")
    fileout = open(filename2, "w")
    rawtext = filein.read()
    lowtext = rawtext.lower()
    for char in lowtext:
        if char in string.ascii_lowercase:
            encryptchar = cipher[char]
            fileout.write(encryptchar)
        else:
            fileout.write(char)
    filein.close()
    fileout.close()


    
# Question 2
# put definition of colorSwap here


def colorSwap(pict):
    """swaps colors in a picture. Green becomes red, blue becomes green, and red becomes blue."""
    swappo = copyPicture(pict)
    for pixel in getPixels(swappo):
        newr = pixel.getGreen()
        newg = pixel.getBlue()
        newb = pixel.getRed()
        pixel.setColor(makeColor(newr, newg, newb))
    return swappo


# Question 3
# put definition of redToCyan here


def redToCyan(pict):
    """replaces areas of an image that are more red than blue or green with cyan"""
    spam = copyPicture(pict)
    for pixel in getPixels(spam):
        r = pixel.getRed()
        g = pixel.getGreen()
        b = pixel.getBlue()
        if r > g and r > b:
            pixel.setColor(makeColor(0, 255, 255))
    return spam
from hw5Code import *
from imageTools import *


def runTests():
    """Remove the # from the following lines to run the tests"""
    encryptTests()
    colorSwapTests()
    redToCyanTests()

# Loads in a couple of images to test with,

p1 = makePicture('redDoor.jpg')
p2 = makePicture('butterfly2.jpg')
p3 = makePicture('caterpillar.jpg')


# ==========================================================================================
# Tests for encrypt

def decrypt(encrypted_file, decrypted_file, cipher):
    fileIn = open(encrypted_file, 'r')
    fileOut = open(decrypted_file, 'w')
    text = fileIn.read()
    text = text.lower()
    for character in text:
        index = cipher.find(character)
        if index !=-1:
            newChar = chr(97+index)
        else:
            newChar = character

        fileOut.write(newChar)
    fileIn.close()
    fileOut.close()

def encryptTests():
    print("--------------------------------------")
    print("Testing encrypt:")

    allOk = True

    cipher13 = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w',
              'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g',
              'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm'}
    encrypt("alice.txt", "encrypt_alice.txt", cipher13)
    s1 = "nopqrstuvwxyzabcdefghijklm"
    decrypt("encrypt_alice.txt", "decrypted_alice.txt", s1)
    fileIn1 = open("alice.txt", 'r')
    fileIn2 = open("decrypted_alice.txt", 'r')
    text1 = fileIn1.read()
    text1 = text1.lower()
    text2 = fileIn2.read()
    if text1 == text2:
        allOk = True
    else:
        print("Test 1 failed.  Visually inspect 'alice.txt' and 'decrypted_alice.txt' for differences.")
        allOk = False

    cipherRand = {'a': 'g', 'b': 'm', 'c': 'c', 'd': 'q', 'e': 'i', 'f': 'r', 'g': 'v', 'h': 'w', 'i': 'z', 'j': 't',
                  'k': 'b', 'l': 'n', 'm': 'p', 'n': 'k', 'o': 'a', 'p': 'f', 'q': 'j', 'r': 'x', 's': 'u', 't': 'y',
                  'u': 'h', 'v': 'o', 'w': 's', 'x': 'd', 'y': 'e', 'z': 'l'}
    encrypt("alice.txt", "encrypt_alice2.txt", cipherRand)
    s2 = "gmcqirvwztbnpkafjxuyhosdel"
    decrypt("encrypt_alice2.txt", "decrypted_alice2.txt", s2)
    fileIn3 = open("alice.txt", 'r')
    fileIn4 = open("decrypted_alice2.txt", 'r')
    text3 = fileIn3.read()
    text3 = text3.lower()
    text4 = fileIn4.read()
    if text3 == text4:
        allOk = True
    else:
        print("Test 2 failed.  Visually inspect 'alice.txt' and 'decrypted_alice2.txt' for differences.")
        allOk = False

    if allOk:
        print("Tests okay")

    print("--------------------------------------")


# ==========================================================================================
# Tests for colorSwap

def colorSwapTests():
    print("--------------------------------------")
    print("Testing colorSwap:")

    allOk = True

    r1 = colorSwap(p1)
    if not isinstance(r1, Picture) or p1 == r1:
        print("Called: colorSwap(p1)")
        print("Expected: a new Picture object, but function returned:", r1)
        allOk = False
    else:
        show(p1)
        show(r1)

    r2 = colorSwap(p2)
    if not isinstance(r2, Picture) or p2 == r2:
        print("Called: colorSwap(p2)")
        print("Expected: a new Picture object, but function returned:", r2)
        allOk = False
    else:
        show(p2)
        show(r2)

    r3 = colorSwap(p3)
    if not isinstance(r3, Picture) or p3 == r3:
        print("Called: colorSwap(p3)")
        print("Expected: a new Picture object, but function returned:", r3)
        allOk = False
    else:
        show(p3)
        show(r3)

    if allOk:
        print("Tests okay")

    print("Check the displayed pictures to see if they look right")
    print("--------------------------------------")


# ==========================================================================================
# Tests for redToCyan

def redToCyanTests():
    print("--------------------------------------")
    print("Testing redToCyan:")

    allOk = True

    r1 = redToCyan(p1)
    if not isinstance(r1, Picture) or p1 == r1:
        print("Called: redToCyan(p1)")
        print("Expected: a new Picture object, but function returned:", r1)
        allOk = False
    else:
        show(p1)
        show(r1)

    r2 = redToCyan(p2)
    if not isinstance(r2, Picture) or p2 == r2:
        print("Called: redToCyan(p2)")
        print("Expected: a new Picture object, but function returned:", r2)
        allOk = False
    else:
        show(p2)
        show(r2)

    r3 = redToCyan(p3)
    if not isinstance(r3, Picture) or p3 == r3:
        print("Called: redToCyan(p3)")
        print("Expected: a new Picture object, but function returned:", r3)
        allOk = False
    else:
        show(p3)
        show(r3)

    if allOk:
        print("Tests okay")

    print("Check the displayed pictures to see if they look right")
    print("--------------------------------------")


runTests()

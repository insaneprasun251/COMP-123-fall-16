
from hw6Code import *
from imageToolsTools import *
# Loads in a couple of images to test with, 

p1 = makePicture('flower2.jpg')
p2 = makePicture('butterfly.jpg')
p3 = makePicture('greekRuins.jpg')
p4 = makePicture('passionflower.jpg')
p5 = makePicture('redmotorcycle.jpg')
p6 = makePicture('bluemotorcycle.jpg')




def runTests():
    """Remove the # from the following lines to run the tests"""
    wallpaperTests()
    upsideDownTests()


# ==========================================================================================
# Tests for wallpaper

def wallpaperTests():
    print("--------------------------------------")
    print("Testing wallpaper:")

    allOk = True

    r1 = wallpaper(p1, 5, 3)
    if not isinstance(r1, Picture):
        print("Called: wallpaper(p1, 5, 3)")
        print("Expected: a new Picture object, but function returned:", r1)
        allOk = False
    else:
        show(r1)
        wait(r1)
        
    r2 = wallpaper(p1, 2, 8)        
    if not isinstance(r2, Picture) :
        print("Called: wallpaper(p1, 2, 8)")
        print("Expected: a new Picture object, but function returned:", r2)
        allOk = False
    else:
        show(r2)
        wait(r2)

    r3 = wallpaper(p2, 1, 1)
    if not isinstance(r3, Picture) :
        print("Called: wallpaper(p2, 1, 1)")
        print("Expected: a new Picture object, but function returned:", r3)
        allOk = False
    else:
        show(r3)
        wait(r3)

    r4 = wallpaper(p3, 2, 2)
    if not isinstance(r4, Picture) :
        print("Called: wallpaper(p3, 2, 2)")
        print("Expected: a new Picture object, but function returned:", r4)
        allOk = False
    else:
        show(r4)
        wait(r4)
    

    if allOk:
        print("Tests okay")


    print("Check the displayed pictures to see if they look right: first should have 5 columns")
    print("and 3 rows, second should be 2 columns and 8 rows, 3rd is just one copy, fourth")
    print("is 2x2 of greek ruins")
    print("--------------------------------------")    





# ==========================================================================================
# Tests for upsideDown

def upsideDownTests():
    print("--------------------------------------")
    print("Testing upsideDown:")

    allOk = True

    r1 = upsideDown(p1)
    if not isinstance(r1, Picture) or p1 == r1:
        print("Called: upsideDown(p1)")
        print("Expected: a new Picture object, but function returned:", r1)
        allOk = False
    else:
        show(p1)
        show(r1)
        wait(r1)
        
    r2 = upsideDown(p2)        
    if not isinstance(r2, Picture) or p2 == r2:
        print("Called: upsideDown(p2)")
        print("Expected: a new Picture object, but function returned:", r2)
        allOk = False
    else:
        show(p2)
        show(r2)
        wait(r2)

    r3 = upsideDown(p3)
    if not isinstance(r3, Picture) or p3 == r3:
        print("Called: upsideDown(p3)")
        print("Expected: a new Picture object, but function returned:", r3)
        allOk = False
    else:
        show(p3)
        show(r3)
        wait(r3)

    r4 = upsideDown(p4)
    if not isinstance(r4, Picture) or p4 == r4:
        print("Called: upsideDown(p4)")
        print("Expected: a new Picture object, but function returned:", r4)
        allOk = False
    else:
        show(p4)
        show(r4)
        wait(r4)
    
    

    if allOk:
        print("Tests okay")


    print("Check the displayed pictures to see if they look right")
    print("--------------------------------------")    

runTests()

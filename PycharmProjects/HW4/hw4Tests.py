
# Change the filename below to match your solution file's name

from hw4Code import *

import turtle
import time # the time module is good for many time related things. we use it to ask python to puase temporarily.


# ========================================================================
# Main tester function. I created this so you only have to make changes
# to this file up here at the top.


def runTests():
    """Uncomment the tests here that you want to run."""
    sportsScoreTests()
    badWordFilterTests()
    cleanTests()
    scrapeNamesTests()

    print("DONE WITH ALL TESTS.")


# ==========================================================================================
# Tests for sportScore

def sportsScoreTests():
    print("--------------------------------------")
    print("Testing sportsScore:")
    soccer = {"kick off": 0, "pass":0, "breakaway":0, "goal": 1}
    football = {"kick off": 0, "first down": 0, "field goal": 3, "touchdown": 6, "extra point": 1}

    r1 = sportsScore({}, [])
    r2 = sportsScore(soccer, [])
    r3 = sportsScore(soccer, ["pass","pass","pass","pass"])
    r4 = sportsScore(soccer, ["kick off", "pass", "pass", "breakaway", "goal", "kick off", "pass", "pass", "goal"])
    r5 = sportsScore(football, ["field goal"])
    r6 = sportsScore(football, ["kick off", "first down", "field goal","kick off", "touchdown", "extra point"])

    allOk = True

    if r1 != 0:
        print("Called: sportsScore({}, [])")
        print("Expected:", 0, "   but function returned:", r1)
        allOk = False
    if r2 != 0:
        print('Called: sportsScore({"kick off":0, "pass":0, "breakaway":0, "goal":1}, []')
        print("Expected:", 0, "   but function returned:", r2)
        allOk = False
    if r3 != 0:
        print('Called: sportsScore({"kick off":0, "pass":0, "breakaway":0, "goal":1}, ["pass","pass","pass","pass"])')
        print("Expected:", 0, "   but function returned:", r3)
        allOk = False
    if r4 != 2:
        print('Called: sportsScore({"kick off":0, "pass":0, "breakaway":0, "goal":1}, ["kick off", "pass", "pass", "breakaway", "goal", "kick off", "pass", "pass", "goal"])')
        print("Expected:", 2, "   but function returned:", r4)
        allOk = False
    if r5 != 3:
        print('Called: sportsScore({"kick off": 0, "first down":0, "field goal":3, "touchdown":6, "extra point":1}, ["field goal"])')
        print("Expected:", 3, "   but function returned:", r5)
        allOk = False
    if r6 != 10:
        print('Called: sportsScore({"kick off": 0, "first down":0, "field goal":3, "touchdown":6, "extra point":1}, "kick off", "first down", "field goal","kick off", "touchdown", "extra point"])')
        print("Expected:", 10, "   but function returned:", r6)
        allOk = False
    if allOk:
        print("Tests okay")
    print("--------------------------------------")


# ==========================================================================================
# Tests for badWordFilter

def badWordFilterTests():
    print("--------------------------------------")
    print("Testing badWordFilter:")

    r1 = badWordFilter("a cat in a hat", ["cat", "hat"])
    e1 = "a <CENSORED> in a <CENSORED>"

    r2 = badWordFilter("a cat in a hat", ["dog", "cap"])
    e2 = "a cat in a hat"

    r3 = badWordFilter("a cat in a hat", ["in"])
    e3 = "a cat <CENSORED> a hat"

    r4 = badWordFilter("hop on pop", ["on"])
    e4 = "hop <CENSORED> pop"

    r5 = badWordFilter("hop on pop", [])
    e5 = "hop on pop"

    r6 = badWordFilter("", ["rat"])
    e6 = ""

    allOk = True

    if r1 != e1:
        print('Called: badWordFilter("a cat in a hat", ["cat","hat"])')
        print("Expected:", e1, "   but function returned:", r1)
        allOk = False
    if r2 != e2:
        print('Called: badWordFilter("a cat in a hat", ["dog","cap"])')
        print("Expected:", e2, "   but function returned:", r2)
        allOk = False
    if r3 != e3:
        print('Called: badWordFilter("a cat in a hat", ["in"])')
        print("Expected:", e3, "   but function returned:", r3)
        allOk = False
    if r4 != e4:
        print('Called: badWordFilter("hop on pop", ["on"])')
        print("Expected:", e4, "   but function returned:", r4)
        allOk = False
    if r5 != e5:
        print('Called: badWordFilter("hop on pop", [])')
        print("Expected:", e5, "   but function returned:", r5)
        allOk = False
    if r6 != e6:
        print('Called: badWordFilter("", ["rat"])')
        print("Expected:", e6, "   but function returned:", r6)
        allOk = False

    if allOk:
        print("Tests okay")

    print("--------------------------------------")

# ==========================================================================================
# Tests for the name-scraping functions


def cleanTests():
    print("--------------------------------------")
    print("Testing clean:")

    r1 = clean(['A', 'man,', 'a', 'plan,', 'a', 'canal:', 'Panama!'])
    r2 = clean(['**foo**', '!@#$!bar%*#(}', "[,.?`baz@#()-+=", '"bats"'])
    r3 = clean(['no', 'punctuation', 'at', 'all'])
    r4 = clean([])

    allOk = True
    
    if r1 != ['A', 'man', 'a', 'plan', 'a', 'canal', 'Panama']:
        print("Called: clean(['A', 'man,', 'a', 'plan,', 'a', 'canal:', 'Panama!'])")
        print("Expected:", ['A', 'man', 'a', 'plan', 'a', 'canal', 'Panama'], "   but function returned:", r1)
        allOk = False
    if r2 != ['foo', 'bar', 'baz', 'bats']:
        print("Called: clean(['**foo**', '!@#$!bar%*#(}', \"[,.?`baz@#()-+=\", '\"bats\"'])")
        print("Expected:", ['foo', 'bar', 'baz', 'bats'], "   but function returned:", r2)
        allOk = False
    if r3 != ['no', 'punctuation', 'at', 'all']:
        print("Called: clean(['no', 'punctuation', 'at', 'all']")
        print("Expected:", ['no', 'punctuation', 'at', 'all'], "   but function returned:", r3)
        allOk = False
    if r4 != []:
        print("Called: clean([])")
        print("Expected:", [], "   but function returned:", r4)
        allOk = False
    

    if allOk:
        print("Tests okay")

    print("--------------------------------------")    


def scrapeNamesTests():
    print("--------------------------------------")
    print("Testing scrapeNames:")

    r1 = scrapeNames('"A man, a plan, a canal: Panama!" is a palindrome that may refer to Teddy Roosevelt.')
    r1ExpResult = {'A': 1, 'Panama': 1, 'Teddy': 1, 'Roosevelt': 1}
    r2 = scrapeNames('Reggie and Mary went to Wales. Mary came home in September, Reggie stayed in Wales until December.')
    r2ExpResult = {'Reggie': 2, 'Mary': 2, 'Wales': 2, 'September': 1, 'December': 1}
    r3 = scrapeNames('no words with capitals whatsoever!')
    r3ExpResult = {}
    r4 = scrapeNames('')
    r4ExpResult = {}
    
    allOk = True
    
    if r1 != r1ExpResult:
        print("Called: scrapeNames('\"A man, a plan, a canal: Panama!\" is a palindrome...')")
        print("Expected:", r1ExpResult, "   but function returned:", r1)
        allOk = False
    if r2 != r2ExpResult:
        print("Called: scrapeNames('Reggie and Mary went to Wales...')")
        print("Expected:", r2ExpResult, "   but function returned:", r2)
        allOk = False
    if r3 != r3ExpResult:
        print("Called: scrapeNames('no words with capitals whatsoever!')")
        print("Expected:", r3ExpResult, "   but function returned:", r3)
        allOk = False
    if r4 != r4ExpResult:
        print("Called: scrapeNames('')")
        print("Expected:", r4ExpResult, "   but function returned:", r4)
        allOk = False
    

    if allOk:
        print("Tests okay")

    print("--------------------------------------")    

runTests()

#  HW4 code file

import turtle
import random


# Question 1

# a, b

# Question 2

def sportsScore(dict, list):
    """takes a dictionary of actions in the game and their point values, then returns the score for a team
    based on a list of strings indicating the moves in the game"""
    score = 0
    for elem in list:
        score = score + dict[elem]
    return score


# Question 3

def badWordFilter(string, badword):
    """filters 'badword' out of the list of words and replaces with '<CENSORED>' in a new string that's
    otherwise identical to the original string"""
    replacement = "<CENSORED>"
    outStr = ""
    textList = string.split()
    for i in range(len(textList)):
        if textList[i] in badword:
            outStr = outStr + replacement + " "
        else:
            outStr = outStr + textList[i]+ " "
    return outStr.strip()


# Question 4

import string


def scrapeNames(text):
    """Takes in a string of text, and splits it into words.  It collect capitalized words in a dictionary
    that keeps track of how often the capitalized words occurred in the text."""
    nameDict = {}                                       # made nameDict a dictionary, not a list--{} instead of []
    words = clean(text.split())                         # added () to split method
    for word in words:
        firstLetter = word[0]                          # fixed word index from 1 to 0 and list reference from words to word
        if firstLetter.isupper():
            if word in nameDict:
                nameDict[word] = nameDict[word] + 1
            else:
                nameDict[word] = 1
    return nameDict


def clean(wordList):
    """Takes in a list of words, and cleans them up: it removes punctuation from the beginning or
    ending of each word, and builds a new list with the results."""
    cleanList = []
    for word in wordList:
        newWord = word.strip(string.punctuation)
        cleanList.append(newWord)                       # changed append to the proper list
    return cleanList                                    # changed incorrect print statement to return

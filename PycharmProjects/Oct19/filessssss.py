# Part 1

file = open("song.txt")
numLines = 0
linesI = 0
for line in file:
    numLines = numLines + 1
    if line[0:2] == "I ":
        print(line[0:-1])
        linesI = linesI + 1
print(linesI)
file.close()

# Part 2

import string


def writeNums(filename, min, max):
    file = open(filename + ".txt", "w")
    for nums in range(min, max + 1):
        file.write(str(nums) + "\n")
    file.close()
writeNums("apple", 10, 21)

def countWords(list):
    stringcount = {}
    for string in list:
        if string in stringcount:
            stringcount[string] = stringcount[string] + 1
        else:
            stringcount[string] = 1
    # for key in stringcount:
    #     if stringcount[key] <= 5:
    #         del stringcount[key]
    return stringcount


def clean(wordList):
    """Takes in a list of words, and cleans them up: it removes punctuation from the beginning or
    ending of each word, and builds a new list with the results."""
    cleanList = []
    for word in wordList:
        newWord = word.strip(string.punctuation)
        cleanList.append(newWord)
    return cleanList



def toWordList(infile):
    file = open(infile + ".txt")
    filestring = file.read()
    wordlist = clean(filestring.split())
    return wordlist

def main():
    worddict = countWords(toWordList("song"))
    for keys in worddict:
        if worddict[keys] >= 5:
            print(keys, ":", worddict[keys])

main()
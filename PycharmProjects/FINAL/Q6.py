# There are two bugs in this program. Your job is to find
# these bugs and fix them. If you want full credit you
# need to do three things for each bug:
# 1. In a comment describe the bug
# 2. Fix the bug
# 3. In a comment describe how you fixed the bug.

def wordCount(fileName):
    """This function computes the word count of a text file
    It does this by reading through the file line by line
    and splitting on white space and counting the resulting
    words"""
    f = open(fileName, 'r')
    wc = 0
    for line in f:
        # line = f.readline()   # this line of code messes with the execution of the for loop, preventing an accurate count.
        line = line.split()
        lineCount = len(line)
        wc = wc + lineCount  # not a proper accumulator pattern; I added each loop's value to the running total to count all the words
    return wc

print(wordCount("manInIronMask.txt"))
# should print 176663


# This question has you write a function named greater.
# The Greater function takes a dictionary whose keys are
# numbers and whose values are numbers. The function
# returns a list of all keys that are larger than their
# values. The original dictionary should not be modified.
# See the included example for more information.

def greater(someDict):
    greaters = []
    for (k, v) in someDict.items():
        if k > v:
            greaters.append(k)
    return greaters


aDict = {1:2, 2:1, 306:306, 4:1, 51:61, 17:3}
print(greater(aDict))
#should print (order may change)
# [2,4,17]
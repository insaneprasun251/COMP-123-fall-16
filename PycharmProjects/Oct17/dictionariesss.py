income = {}

age = {"Daniel": 27, "Julius": 23, "Debra": 5}

print(age["Daniel"])

age["Henry"] = 43

print(age)

age2 = age.copy()

del age2["Henry"]

age3 = age2

print("Henry" in age)
print("Henry" in age2)
print("Henry" in age3)


def valReset(name, dict):
    dict[name] = 0

animals = {'Sir Reginald Fluffybottom': 'dog',
           'Fog': 'cat',
           'Dr. Pepper': 'cat',
           'Pepsi': 'cat',
           'Dana': 'dog',
           'foo': 'dog',
           'bar': 'dog'}


def countAnimals(animalDict, type):
    number = 0
    for values in animalDict.values():
        if values == type:
            number = number + 1
    return number


print(countAnimals(animals, 'cat'))

import math


def smallestThing(list):
    small = math.inf
    for value in list:
        if value < small:
            small = value
    return small

def smallestVal(dict):
    small = math.inf
    for value in dict.values():
        if value < small:
            small = value
    return small

def smallestValKey(dict):
    smallKey = ""
    smallVal = math.inf
    for key in dict.keys():
        if dict[key] < smallVal:
            smallKey = key
            smallVal = dict[key]
    return smallKey

print(smallestVal(age))
print(smallestValKey(age))
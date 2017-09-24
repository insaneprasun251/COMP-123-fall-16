#Part One

def squareMinusOne(input):
    """"Input parameter is multiplied by itself. 1 subtracted from the result and returned as output"""

    output = input*input-1
    return output

#Part Two

print("1 squared minus one is", squareMinusOne(1), "It should be 0")
print("2 squared minus one is", squareMinusOne(2), "it should be 3")
print("3 squared minus one is", squareMinusOne(3), "it should be 8")
print("4 squared minus one is", squareMinusOne(4), "It should be 15")

#Part Three

def smallestDiff(a, b, c):
    """smallestDiff computes the smallest difference between the numbers given to it.
    It does this by taking the absolute value of of the differences of the three pairs of numbers,
    then returning the smallest of those values"""
    pairOne = abs(a-b)
    pairTwo = abs(b-c)
    pairThree = abs(a-c)
    return min(pairOne, pairTwo, pairThree)

#Part Four

print(smallestDiff(1, 2, 2))
print(smallestDiff(1, 3, 4))
print(smallestDiff(100, 23, 104))
print(smallestDiff(9, 98, 40))
print(smallestDiff(26, 92, 90))

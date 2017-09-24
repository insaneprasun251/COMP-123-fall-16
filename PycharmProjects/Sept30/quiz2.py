import math

# Question 1

# As this code does not work I have provided it commented out.
# To begin Question 1 you should first uncomment this code by
# deleting the # characters from the beginning of each line (starting at the def)
# included in this file is also code to run the relative function with different
# inputs and a description of exactly what it should print (no more no less)
# when the code is correct.


def relative(a, b, x):
    """ This function returns "left" "middle" or "right" to
    describe if point x is less than a and b (left), inbetween a
    and b (middle) or greater than a and b. (right) """
    if x <= a and x <= b:                               # Changed or to and; both conditions must be True for the function to work
        return 'left'                                   # Changed print to return to avoid lines printing None
    elif (a <= x and x <= b) or (b <= x and x <= a):    # Changed to elif statement
        return 'middle'                                 # Changed print to return to avoid lines printing None
    else:                                               # Missing : after else
        return 'right'                                  # Changed print to return to avoid lines printing None


print(relative(2,4,1)) # left
print(relative(4,2,1)) # left
print(relative(2,4,3)) # middle
print(relative(4,2,3)) # middle
print(relative(2,4,5)) # right
print(relative(4,2,5)) # right

#
print()
#

# Question 2


def countNumber(n):
    accum = ""
    for i in range(1, n + 1):
        accum = accum + str(i)
    return accum

print(countNumber(6))

#
print()
#

# Question 3


def isSquare(length, width):
    return length == width

print(isSquare(17,17))
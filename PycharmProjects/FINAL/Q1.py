# In this question you are provided a function to determine
# if a string is a palindrome. This function is recursive
# you have several tasks

# 1. Using comments, label each line of code as either
# part of a base case or a recursive case. If there are
# more than one base case or recursive case number the
# cases (I.E. base case 1)

# 2. For each case, explain the case. For base cases,
# please explain what the case is (under what conditions
# the case gets ran) and why the base case is correct
# (the conditions under which the base case is ran, why
# is it correct to return what it does).
# For recursive cases explain in what way the recursive
# call moves closer to a base case.

def palindrome(aString):
    """This function takes a string and returns True
    if the string is a palindrome. (A palindrome is
    any string that is the same forwards and backwards)
    examples: 'a', 'abba', 'qwe r ewq'"""
    if len(aString) <= 1:  # base case 1: if the string is 1 character or less it must be a palindrome
        return True
    elif aString[0] != aString[-1]:  # base case 2: if the first and last letters of the string are not the same, the string cannot be a palindrome.
        return False
    else:
        return palindrome(aString[1:len(aString)-1])  # recursive case: if the first and last letters of the string are the same, proceed to test the second and second to last letters with the same criteria

print(palindrome(""))  # True               len < 1, it must be a palindrome
print(palindrome("abba"))  # True           first and last letters are the same; 2nd and 2nd to last letters are the same in the recursion
print(palindrome("apa"))  # True            first and last letters are the same; in the recursive call, the remaining string is 1 char long
print(palindrome("!"))  # True              len = 1, it must be a palindrome
print(palindrome("ape"))  # False           first and last letters are not the same
print(palindrome("as"))  # False            first and last letters are not the same
print(palindrome("aaaapeaaa"))  # False     outer letters on the third recursion are not the same
def reverseModify(lst):
    """Reverse a list in place by swapping elements"""
    for i in range(len(lst)//2):
        # swap first and last and so forth
        tmp = lst[i]
        lst[i] = lst[len(lst)-1-i]
        lst[len(lst)-1-i] = tmp

def reversePure(lst):
    """Return the reverse of a list"""
    newList = []
    for elem in lst:
        newList.insert(0, elem)
    return newList

lst = [1,2,3,4,5]
print("lst:",lst)

print("calling reverseModify(lst)")
out = reverseModify(lst)
print("out:",out)
print("lst:",lst)

print("calling reversePure(lst)")
out = reversePure(lst)
print("out:",out)
print("lst:",lst)
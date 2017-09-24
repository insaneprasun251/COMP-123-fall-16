# part 1


def readfile(filename):
    """returns contents of specified file as a string"""
    file = open(filename, 'r')
    outstr = ""
    for lines in file:
        outstr = outstr + lines
    file.close()
    return outstr

# part 2


def writefile(filename, contents):
    """writes contents to specified file"""
    file = open(filename, 'w')
    file.write(contents)
    file.close()


# part 3


def searchdict(dict, value):
    """finds all keys in a dictionary with a given value"""
    thing = []
    for (k, v) in dict.items():
        if v == value:
            thing = thing + [k]
    return thing

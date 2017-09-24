def rot13_letter(inLetter):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    inLetter = inLetter.upper()
    if inLetter in alphabet:
        letterIndex = alphabet.find(inLetter)
        letterIndex = (letterIndex + 13)%26
        return alphabet[letterIndex]
    else:
        return inLetter


def rot13(inString):
    # basic accumulation string pattern.
    outString = ""
    for oldLetter in inString:
        # convert each letter one at a time.
        newLetter = rot13_letter(oldLetter)
        # add the new letter to the output string and store result
        outString = outString + newLetter
    return outString

print("apples to apples")
print(rot13("apples to apples"))
print(rot13(rot13("apples to apples")))

class MyClass:
    def __init__(self, pre, num):
        self.prefix = pre
        self.numEchoes = num
        print("creating new MyClass", pre)

    def echo(self, words):
        for i in range(self.numEchoes):
            print(self.prefix, words)

    def echotwice(self, words):
        print(words, words)

def myClassTests():
    t = MyClass("prefix-for-t", 7)
    t.echo("donkey")
    t.echotwice("donkey")
    print(t.prefix)


    s = MyClass()
    s.echo("Shrek!")
    s.echotwice("Shrek!")


class Adder:
    def __init__(self, startingValue):
        print("creating new Adder")
        self.value = startingValue

    def getValue(self):
        return self.value

    def addValue(self, additionalValue):
        self.value = self.getValue() + additionalValue
        return self.value

    def removeValue(self, removedValue):
        self.value = self.getValue() - removedValue
        return self.value

    # def transferValue(self, anotherAdder):
    #     v1 = self.value
    #     anotherAdder.value = anotherAdder.value + v1
    #     print(v1)
    #     self.value = 0
    #     return self.value, anotherAdder.value


class Fraction:
    def __init__(self, num, denom):
        self.numerator = num
        self.denominator = denom
        print("Fraction:", self.numerator, "/", self.denominator)

    def getNumerator(self):
        return self.numerator


    def getDenominator(self):
        return self.denominator


    def fractionToFloat(self):
        return self.numerator / self.denominator


def main():
    account = Adder(0)
    print(account.value)
    print(account.getValue())
    account2 = account.addValue(15)
    print(account2)
    account2 = account.removeValue(22)
    print(account2)
    # account3 = account.transferValue(account2)
    # print(account3)

    frac = Fraction(2, 5)
    q = frac.getNumerator()
    r = frac.getDenominator()
    s = frac.fractionToFloat()
    print(q)
    print(r)
    print(s)

main()
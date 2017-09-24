def makeChange(money):
    dollars = int(money)
    money = money - dollars
    quarters = int(money/0.25)
    money = money - 0.25*quarters
    dimes = int(money/0.10)
    money = money -0.1*dimes
    nickels = int(money*100/5)
    money = money - nickels*0.05
    pennies = int(money*100)
    print(dollars, quarters, dimes, nickels, pennies)

makeChange(10.45)

1+1


def isPrime(n):
    """this function returns 0 if a number is not prime and 1 otherwise."""

    retval = 1
    for i in range(2, n):
        retval = min(retval, n%i)
    return retval

print(isPrime(17))

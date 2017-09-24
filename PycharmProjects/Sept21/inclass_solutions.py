ready = "dog"

import math


def dubSqrRoot(bar):
    foo = bar*2
    foo = math.sqrt(foo)
    return int(foo)


def square(trt):
    for i in range(4):
        trt.fd(100)
        trt.rt(90)


def largePrime(n):
    accum = 1
    for i in range(1, n+1):
        accum = accum*i
    accum = accum+1
    return accum

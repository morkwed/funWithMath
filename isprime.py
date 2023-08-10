import math
# a function for checking if a number is prime
def isPrime (arg):
    n = round(math.sqrt(arg),0)
    while (n > 1):
        if (arg % n == 0):
            return (False)
        else:
            n -= 1
    return (True)

from RSA.entity.private import Private
from RSA.entity.public import Public
from RSA.entity.crypto import Crypto
from miller_rabin import miller_rabin
import random

def getPrime(min, max):
    """
    Return a prime number in a range
    """
    n = 1
    while miller_rabin(n) != True:
        n = random.randrange(min, max)
    return n

def gcd(a, b):
    """
    Performs the Euclidean algorithm and returns the gcd of a and b
    """
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)

def xgcd(a, b):
    """
    Performs the extended Euclidean algorithm
    Returns the gcd, coefficient of a, and coefficient of b
    """
    x, old_x = 0, 1
    y, old_y = 1, 0

    while (b != 0):
        quotient = a // b
        a, b = b, a - quotient * b
        old_x, x = x, old_x - quotient * x
        old_y, y = y, old_y - quotient * y

    return a, old_x, old_y

def getE(t):
    """
    Return a number that is greater than 1 and is co-prime of t
    """
    i=2
    while(gcd(i, t) != 1):
        i += 1
    return i

def getD(e, t):
    """
    Return a number that inverse of e and also co-prime of t
    """
    g, x, y = xgcd(e, t)
    if(x < 0):
        d = x + t
    else: 
        d = x
    return d

class CreateKeys:
    def __init__(self) -> None:
        pass

    def execute(min, max):
        p = getPrime(min, max)
        q = getPrime(p+min,p+max)
        print("Prime p: ", p)
        print("Prime q: ", q)
        n = p * q
        t = (p-1)*(q-1)
        e = getE(t)
        d = getD(e, t)

        #return Crypto(n, e, d)
        return Public(n, e), Private(n, d)
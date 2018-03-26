import math

def isPrimeNumber(number):
    int_number = int(number)
    for i in xrange(int_number-1):
        if i > 3 and int_number%i == 0:
            return False, i
    return True, 0

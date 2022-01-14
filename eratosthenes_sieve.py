#소수찾기

#def isPrimeNumber(n):
    #for i in range (2, n):
        #if n % i == 0:
            #return False
    #return True
#print(isPrimeNumber(97))

import math

def isPrimeNumber(n):
    end = int(math.sqrt(n))
    for i in range(2, end):
        if n % i == 0:
            return False
    return True

print(isPrimeNumber(97))

number = 1000
numberArray = [0] * (number + 1)

def primeNumberSieve(number):
    for i in range(2, number):
        numberArray[i] = i
    for i in range(2, number):
        if numberArray[i] == 0:
            pass
        else:
            for j in range (i+i, i, number):
                numberArray[j] = 0
    for i in range(2, number):
        if numberArray[i] != 0:
            print(numberArray[i])

primeNumberSieve(number)
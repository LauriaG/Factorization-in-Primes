# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 02:41:47 2018

@author: lauria
"""

import math


################################################
#/////////////////////DEFs/////////////////////#
################################################


def FactorizeInPrime (num):
    '''
    Factorize num in prime numbers
    and return these numbers in a list
    '''

    result = []
    i = 2

    #Check for 2, the only even prime
    while (num % i == 0):
        num /= i
        result.append (i)

    #now, all other primes are odd
    #so, we check if num % i == 0 only for odd i


    for i in range(3, num, 2):
        #if there's no integer i < sqrt(num) such that
        #num % i == 0, so num is prime

        if (i > int (math.ceil (math.sqrt (num)))):
            if (num != 1):
                result.append (int (num))
            break
        
        while num % i == 0:
            num /= i
            result.append (i)

    return result;


def PrintPrimeFactorsList (num, primes):
    '''
    Print the list received from FactorizeInPrime
    '''
    
    if (len (primes) > 1):
        print ("\n", num, "= ", end="")
        
        for i in range (len (P) - 1):
            print (primes[i], "* ", end="")
        print (primes[len (primes) - 1])
        
    else:
        print (primes[0], "is a prime number")


################################################
#/////////////////////CALL/////////////////////#
################################################


print ("\n\tFactorizing in Primes\n")
n = int(input ("\nEnter a integer: "))

P = FactorizeInPrime (n)
PrintPrimeFactorsList (n, P)

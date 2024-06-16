#!/usr/bin/python3

"""
achieve a given number of characters using only
“Copy All” and “Paste” operations
"""


def isPrime(n):
    """finding if number is prime or not
    used as helper to min operation function"""

    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def minOperations(n):
    """find min operation"""
    sum = 0
    list_of_sum = []

    for i in range(2, n+1):
        while (n % i == 0) and isPrime(i):
            list_of_sum.append(i)
            n = n // i

    for i in list_of_sum:
        sum += i
    return sum

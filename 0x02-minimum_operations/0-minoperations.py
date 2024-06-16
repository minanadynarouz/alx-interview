#!/usr/bin/python3

"""
achieve a given number of characters using only
“Copy All” and “Paste” operations
"""


def isPrime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def minOperations(n):
    """Calculate the sum of prime factors of n."""
    if n <= 1:
        return 0

    sum = 0
    i = 2
    while i * i <= n:
        while n % i == 0:
            sum += i
            n //= i
        i += 1

    # If n becomes a prime number greater than 2
    if n > 1:
        sum += n

    return sum

#!/usr/bin/python3

'''Change making problem'''


def makeChange(coins, total):

    if total <= 0:
        return 0

    counter = 0

    for i in sorted(coins, reverse=True):
        while total >= i:
            total -= i
            counter += 1

    if (total < 0 or total > 0):
        return -1
    else:
        return counter

#!/usr/bin/python3

"""
Method to determine if all boxes can be opened
Using prototype: def canUnlockAll(boxes)
"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be unlocked"""

    n = len(boxes)
    opened = [False] * n
    opened[0] = True

    for box in boxes:
        for key in box:
            if key < n:
                opened[key] = True

    if all(opened):
        return True
    else:
        return False

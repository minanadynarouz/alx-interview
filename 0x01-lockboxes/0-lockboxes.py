#!/usr/bin/python3

"""
Method to determine if all boxes can be opened
Using prototype: def canUnlockAll(boxes)
"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be unlocked"""

    n = len(boxes)
    opened = [False] * n

    for box in boxes:
        for key in box:
            if key < n:
                opened[key] = True

    if all(opened):
        return True
    else:
        return False


boxes = [[7, 5], [1, 10, 7], [9, 6, 10], [7, 9], [2], [7, 3], [
    7, 9, 10, 10, 8, 9, 2, 5], [7, 2, 2, 4, 4, 2, 4, 8, 7], [4, 2, 9, 6, 6, 5, 5], ]

print(canUnlockAll(boxes))

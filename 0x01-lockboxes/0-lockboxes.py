def canUnlockAll(boxes):
    n = len(boxes)
    opened = [False] * n
    opened[0] = True

    for box in boxes:
        for key in box:
            if opened[key]:
                opened[key] = True

    if all(opened):
        return True
    return False


boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

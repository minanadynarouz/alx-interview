#!/usr/bin/python3


"""This function check if data is urf-8 or not"""


def validUTF8(data):
    num_bytes = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        mask = 1 << 7
        if num_bytes == 0:
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1

            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False
        num_bytes -= 1

    return num_bytes == 0

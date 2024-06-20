#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics
"""

import fileinput
import signal
import sys

newDict = {}
counter = 0
total_filesize = 0

def print_stats():
    print("File Size:", total_filesize)
    for code in sorted(newDict.keys()):
        if code != 'File Size':
            print("{}: {}".format(code, newDict[code]))

def process_line(line):
    global counter, total_filesize
    status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']

    split_line = line.split()
    if len(split_line) < 2:
        return

    try:
        filesize = int(split_line[-1])
        total_filesize += filesize
        stream_status_code = split_line[-2]

        if stream_status_code in status_codes:
            if stream_status_code in newDict:
                newDict[stream_status_code] += 1
            else:
                newDict[stream_status_code] = 1
    except ValueError:
        return

    counter += 1
    if counter == 10:
        print_stats()
        counter = 0

def sig_handler(signum, frame):
    print_stats()
    sys.exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, sig_handler)
    try:
        for line in fileinput.input():
            process_line(line)
    except KeyboardInterrupt:
        sig_handler(signal.SIGINT, None)

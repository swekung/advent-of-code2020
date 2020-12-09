import sys
import re
import numpy as np
import time
start_time = time.time()

def readFile(file):
    text = open(file)
    temp = []
    for line in text:
        temp.append(int(line.strip()))
    out = np.array(temp)
    text.close()
    return out

def findInvalid(arr):
    for i in range(25, len(arr)):
        temp = np.array(arr[i-25:i])
        sums = np.add.outer(temp, temp)
        if not arr[i] in sums:
            return i
    return "Not found"


def main():
    arr = readFile("Day 9\input.txt")
    print(findInvalid(arr))


main()
print("--- %s seconds ---" % (time.time() - start_time))
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

def countDiff(arr):
    diff1 = 0
    diff3 = 1
    arr = np.sort(arr)
    for i in range(len(arr) - 1):
        if i == 0:
            if arr[i] == 1:
                diff1 += 1
            elif arr[i] == 3:
                diff3 += 1
        if arr[i+1] - arr[i] == 1:
            diff1 += 1
        elif arr[i+1] - arr[i] == 3:
            diff3 += 1
    return diff1, diff3

def main():
    arr = readFile("Day 10\input.txt")
    diff1, diff3 = countDiff(arr)
    print(diff1 * diff3)


main()
print("--- %s seconds ---" % (time.time() - start_time))
import sys
import re
import numpy as np
import numpy.ma as ma
import scipy.signal
import copy
import time
start_time = time.time()

def readFile(file):
    text = open(file)
    temp = []
    for line in text:
        temp2 = []
        for char in line:
            if char == "L":
                temp2.append(0)
            elif char == "#":
                temp2.append(1)
            elif char == ".":
                temp2.append(-1)
        temp.append(temp2)
    out = np.array(temp)
    text.close()
    return out

def flip(oldarr):
    arr = copy.deepcopy(oldarr)
    isOccupied = arr[1][1]
    arr[1][1] = 0
    empty = 0
    full = 0
    for i in range(len(arr)):
        for j in range(len(arr[1])):
            if arr[i][j] == -1:
                pass
            elif arr[i][j] == 1:
                full += 1
            else:
                empty += 1
    if isOccupied == 1 and full >= 4:
        return 0
    elif not isOccupied == 1 and full == 0:
        return 1
    else:
        return isOccupied


def adjSum(oldarr):
    arr = copy.deepcopy(oldarr)
    arr = np.pad(arr, (1,1), 'constant', constant_values=(-1, -1))
    temp = np.zeros((len(arr) - 2, len(arr) - 2))
    for i in range(1, len(arr) - 1):
        for j in range(1, len(arr[i]) - 1):
            if arr[i][j] == -1:
                temp[i-1][j-1] = -1
            else:
                temp[i-1][j-1] = flip(arr[i - 1 : i + 2, j - 1 : j + 2])
    return temp

def main():
    arr = readFile("Day 11\input.txt")
    areEqual = False
    lastArr = adjSum(arr)
    arr = adjSum(lastArr)
    while not areEqual:
        lastArr = copy.deepcopy(arr)
        arr = adjSum(arr)
        areEqual = np.array_equal(lastArr, arr)

    print(np.count_nonzero(arr == 1))
    print(arr)


main()
print("--- %s seconds ---" % (time.time() - start_time))
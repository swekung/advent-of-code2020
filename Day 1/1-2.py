import numpy as np
import sys
import time
start_time = time.time()

def readFile(file):
    text = open(file)
    out = []
    for line in text:
        out.append(int(line.rstrip('\n')))
    out = np.array(out)
    text.close()
    return out

def findPairs(arr):
    sums = np.add.outer(arr, arr)
    sums = np.add.outer(sums, arr)
    index = np.where(sums == 2020)
    return index[0]

def __main__():
    file = "input.txt"
    arr = readFile(file)
    pair = findPairs(arr)
    print(arr[pair[0]] * arr[pair[2]] * arr[pair[4]])


__main__()
print("--- %s seconds ---" % (time.time() - start_time))
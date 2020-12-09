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

def findContigous(arr, invalidNum, invalidNumIndex):
    for i in range(invalidNumIndex):
        for j in range(invalidNumIndex):
            temp = np.array(arr[i:j])
            sums = np.sum(temp)
            if sums == invalidNum:
                return np.amin(temp) + np.amax(temp)
    return "Not found"

def findContigousOpt(arr, invalidNum, invalidNumIndex):
    for i in range(invalidNumIndex):
        temp = np.array(arr[i:])
        sums = np.cumsum(temp)
        if invalidNum in sums:
            index = np.where(sums == invalidNum)
            temp = temp[:index[0][0] + 1]
            print( np.amax(temp) + np.amin(temp))
    return "Not found"

def main():
    invalidNum = 27911108
    invalidNumIndex = 509
    arr = readFile("Day 9\input.txt")
    #print(findContigous(arr, invalidNum, invalidNumIndex))
    findContigousOpt(arr, invalidNum, invalidNumIndex)

main()
print("--- %s seconds ---" % (time.time() - start_time))
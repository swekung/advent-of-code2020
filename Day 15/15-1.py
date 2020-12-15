import sys
import numpy as np
import time
start_time = time.time()

def readFile(file):
    text = open(file)
    temp = []
    for line in text:
        str = line.strip()
        temp.append(str.split(","))
    out = np.array(temp[0], dtype="int64")
    text.close()
    return out

def playGame(arr, lastRound):
    for i in range(len(arr), lastRound):
        if arr[-1] in arr[:-1]:
            lastIndex = np.where(arr == arr[-1])
            arr = np.append(arr, (i-1) - lastIndex[0][-2])
        else:
            arr = np.append(arr, 0)
        if i % 10000 == 0:
            print(i)
    return arr

def main():
    arr = readFile("Day 15\input.txt")
    arr = playGame(arr, 2020)
    print(arr[-1])


main()
print("--- %s seconds ---" % (time.time() - start_time))
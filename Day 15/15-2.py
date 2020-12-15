import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import time
start_time = time.time()

def readFile(file):
    text = open(file)
    temp = []
    for line in text:
        str = line.strip()
        temp.append(str.split(","))
    text.close()
    return temp[0]

# def playGame(arr, lastRound):
#     for i in range(len(arr), lastRound):
#         if arr[-1] in arr[:-1]:
#             lastIndex = np.where(arr == arr[-1])
#             arr = np.append(arr, (i-1) - lastIndex[0][-2])
#         else:
#             arr = np.append(arr, 0)
#         if i % 10000 == 0:
#             print(i)
#     return arr

def playGame(arr, lastRound):
    startLen = len(arr)
    lastSaid = {}
    lastNum = int(arr[-1])
    for i in range(len(arr) - 1):
        lastSaid[int(arr[i])] = i
    for i in range(startLen, lastRound):
        if not lastNum in lastSaid:
            lastSaid[lastNum] = i-1
            lastNum = 0
        else:
            temp = lastSaid[lastNum]
            lastSaid[lastNum] = i-1
            lastNum = i-1 - temp
    return lastNum



def main():
    arr = readFile("Day 15\input.txt")
    arr = playGame(arr, 30000000)
    # fig, ax = plt.subplots()
    # ax.plot(arr)
    # plt.show()
    print(arr)


main()
print("--- %s seconds ---" % (time.time() - start_time))
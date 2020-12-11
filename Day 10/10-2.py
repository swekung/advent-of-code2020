import sys
import re
import numpy as np
from numpy.linalg import matrix_power
import time
start_time = time.time()

def readFile(file):
    text = open(file)
    temp = []
    for line in text:
        temp.append(int(line.strip()))
    temp.append(max(temp) + 3)
    temp.insert(0, 0)
    out = np.array(temp)
    text.close()
    return out

dyn = {}
def ways(ads):
    if len(ads) in dyn:
        return(dyn[len(ads)])
    if len(ads) <= 1:
        return 1
    i = 1
    tot = 0
    while i < len(ads) and ads[i] <= ads[0] + 3:
        tot += ways(ads[i:])
        i += 1
    dyn[len(ads)] = tot
    return tot


# def countRoutes(arr):
#     permutations = np.zeros(len(arr))
#     arr = np.sort(arr)
#     for i in range(len(arr) - 3):
#         if i == 0:
#             for j in range(1, 4):
#                 if arr[i+j] - 0 <= 3:
#                     permutations[i] += 1
#         for j in range(1, 4):
#             if arr[i+j] - arr[i] <= 3:
#                 permutations[i] += 1
#     for i in range()
#     return permutations

def main():
    arr = readFile("Day 10\input.txt")
    diff1 = ways(np.sort(arr))
    print(diff1)


main()
print("--- %s seconds ---" % (time.time() - start_time))
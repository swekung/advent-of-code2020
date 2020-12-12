import sys
import re
import numpy as np
import time
start_time = time.time()

def readFile(file):
    text = open(file)
    temp = []
    for line in text:
        temp.append(line.strip())
    text.close()
    return temp

def goDirr(coord, dirr, dist):
    if dirr == "N":
         coord[0] += dist   
    elif dirr == "S":
        coord[0] -= dist
    elif dirr == "E":
        coord[1] += dist
    elif dirr == "W":
        coord[1] -= dist
    return coord

def goRoute(arr):
    coord = [0 ,0]
    dirr = 90
    comp = {0: "N", 90: "E", 180: "S", 270: "W"}
    for line in arr:
        if line[0] == "F":
            coord = goDirr(coord, comp[dirr], int(line[1:]))
        elif line[0] == "R":
            dirr += int(line[1:])
            dirr = dirr % 360
        elif line[0] == "L":
            dirr -= int(line[1:])
            dirr = dirr % 360
        else:
            coord = goDirr(coord, line[0], int(line[1:]))
    return coord

def main():
    arr = readFile("Day 12\input.txt")
    coord = goRoute(arr)
    print(abs(coord[0]) + abs(coord[1]))


main()
print("--- %s seconds ---" % (time.time() - start_time))
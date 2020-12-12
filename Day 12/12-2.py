import sys
import re
import numpy as np
import math
import time
start_time = time.time()

def readFile(file):
    text = open(file)
    temp = []
    for line in text:
        temp.append(line.strip())
    text.close()
    return temp

def moveCoord(coord, dirr, dist):
    if dirr == "N":
         coord[0] += dist   
    elif dirr == "S":
        coord[0] -= dist
    elif dirr == "E":
        coord[1] += dist
    elif dirr == "W":
        coord[1] -= dist
    return coord

def rotateCoord(coords, angle):
    angle = np.deg2rad(angle)
    x = coords[0] * math.cos(angle) - coords[1] * math.sin(angle)
    y = coords[0] * math.sin(angle) + coords[1] * math.cos(angle)
    return [int(round(x)), int(round(y))]

def goRoute(arr):
    absCoord = [0 ,0]
    wayCoord = [1, 10]
    dirr = 90
    comp = {0: "N", 90: "E", 180: "S", 270: "W"}
    for line in arr:
        if line[0] == "F":
            absCoord = moveCoord(absCoord, "N", wayCoord[0] * int(line[1:]))
            absCoord = moveCoord(absCoord, "E", wayCoord[1] * int(line[1:]))
        elif line[0] == "R":
            wayCoord = rotateCoord(wayCoord, int(line[1:]))
        elif line[0] == "L":
            wayCoord = rotateCoord(wayCoord, -int(line[1:]))
        else:
            wayCoord = moveCoord(wayCoord, line[0], int(line[1:]))
    return absCoord

def main():
    arr = readFile("Day 12\input.txt")
    coord = goRoute(arr)
    print(abs(coord[0]) + abs(coord[1]))


main()
print("--- %s seconds ---" % (time.time() - start_time))
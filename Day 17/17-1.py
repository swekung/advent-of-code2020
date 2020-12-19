import sys
import numpy as np
from copy import copy
import time
start_time = time.time()

def readFile(file):
    text = open(file)
    temp = []
    for line in text:
        string = line.strip()
        temp.append(list(string))
    text.close()
    out = {}
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            coord = str(i) + "," + str(j) + ",0"
            out[coord] = temp[i][j]
    return out

def countAdj(cubes, coord):
    coords = coord.split(",")
    active = 0
    inactive = 0
    for x in range(int(coords[0]) - 1, int(coords[0]) + 2):
        for y in range(int(coords[1]) - 1, int(coords[1]) + 2):
            for z in range(int(coords[2]) - 1, int(coords[2]) + 2):
                string = "".join([str(x), ",", str(y),",", str(z)])
                if string in cubes and not string == coord:    
                    if cubes[string] == "#":
                        active += 1
                    elif cubes[string] == ".":
                        inactive += 1
                elif not string in cubes and not string == coord:
                    inactive += 1
    return active, inactive

def strCoord2intCoord(coord):
    coords = coord.split(",")
    x = int(coords[0])
    y = int(coords[1])
    z = int(coords[2])
    return x, y, z

def coordsAround(coord):
    x, y, z = strCoord2intCoord(coord)
    out = []
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            for k in range(z-1, z+2):
                out.append("".join([str(i), ",", str(j), ",", str(k)]))
    return out

def cycle(cubes, cycles):
    for i in range(cycles):
        cubeCopy = copy(cubes)
        coords = cubes.keys()
        coordsCopy = []
        for coord in coords:
            coordsCopy += coordsAround(coord)
        coordsCopy = list(dict.fromkeys(coordsCopy))
        for coord in coordsCopy:
            actAdj, inActAdj = countAdj(cubes, coord)
            if not coord in cubes and actAdj == 3:
                cubeCopy[coord] = "#"
            elif not coord in cubes:
                #cubeCopy[coord] = "."
                pass
            elif cubes[coord] == "#":
                if actAdj <= 3 and actAdj >= 2:
                    cubeCopy[coord] = "#"
                elif coord in cubeCopy:
                    #cubeCopy[coord] = "."
                    cubeCopy.pop(coord)
            elif cubes[coord] == ".":
                if actAdj == 3:
                    cubeCopy[coord] = "#"
                elif coord in cubeCopy:
                    #cubeCopy[coord] = "."
                    cubeCopy.pop(coord)
        cubes = copy(cubeCopy)
        
    return cubes




def main():
    cubes = readFile("Day 17\input.txt")
    print(len(cycle(cubes, 6)))


main()
print("--- %s seconds ---" % (time.time() - start_time))
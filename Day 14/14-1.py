import sys
import numpy as np
import re
import time
start_time = time.time()

def readFile(file):
    text = open(file)
    temp = []
    for line in text:
        str = line.strip()
        temp.append(str.split(" "))
    text.close()
    return temp

def parseFile(arr):
    for line in arr:
        if "mask" in line:
            line = [line[0], line[2]]
        else:
            line[2] = bin(int(line[2]))[2:]
            line[2] = line[2].rjust(36, "0")
            line[2] = list(line[2])
            line[0] = int(re.findall("\d+", line[0])[0])
            line = [line[0], line[2]]
    mask = ""
    for line in arr:
        if "mask" in line:
            mask = line[2]
        else:
            for i in range(len(mask)):
                if not mask[i] == "X":
                    line[2][i] = mask[i]
    return arr

def initMem(arr, mem):
    for line in arr:
        if not "mask" in line:
            mem[line[0]] = int("0b" + "".join([str(elem) for elem in line[2]]), 2)
    return mem


def main():
    arr = readFile("Day 14\input.txt")
    mem = {}
    parseFile(arr)
    mem = initMem(arr, mem)
    print(sum(mem.values()))


main()
print("--- %s seconds ---" % (time.time() - start_time))
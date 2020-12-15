import sys
import numpy as np
import re
import time
from copy import copy
start_time = time.time()


def readFile(file):
    text = open(file)
    temp = []
    for line in text:
        str = line.strip()
        temp.append(str.split(" "))
    text.close()
    return temp

def flatten(arr):
    rt = []
    res = []
    for i in arr:
        if isinstance(i,list): rt.extend(flatten(i))
        else: rt.append(i)
    for i in rt: 
        if i not in res: 
            res.append(i) 
    return res

def bin2int(string):
    return int("0b" + string, 2)

def findPerm(mem, mask, i):
    perms = []
    newMem = copy(mem)
    if i == len(mask):
        return "".join(newMem)
    for i in range(i, len(mask)):
        if mask[i] == "X":
            newMem[i] = "1"
            perms.append(findPerm(newMem, mask, i + 1))
            newMem[i] = "0"
            perms.append(findPerm(newMem, mask, i + 1))
        elif mask[i] == "0":
            pass
            #perms.append(findPerm(mem, mask, i))
        else:
            newMem[i] = "1"
            #perms.append(findPerm(mem, mask, i))
    perms.append("".join(newMem))
    return flatten(perms)

def parseFile(arr):
    for line in arr:
        if "mask" in line:
            line = [line[0], line[2]]
        else:
            line[0] = int(re.findall("\d+", line[0])[0])
            line[0] = bin(int(line[0]))[2:]
            line[0] = line[0].rjust(36, "0")
            line[0] = list(line[0])
            line = [line[0], line[2]]
    mask = ""
    for line in arr:
        if "mask" in line:
            mask = line[2]
        else:
            addr = findPerm(line[0], mask, 0)
            line[0] = addr       
    return arr


def initMem(arr, mem):
    for line in arr:
        if not "mask" in line:
            for addr in line[0]:
                mem[bin2int(addr)] = int(line[2])
    return mem


def main():
    arr = readFile("Day 14\input.txt")
    mem = {}
    arr = parseFile(arr)
    print(arr[1][0])
    mem = initMem(arr, mem)

    print(sum(mem.values()))


main()
print("--- %s seconds ---" % (time.time() - start_time))
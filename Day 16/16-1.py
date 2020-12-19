import sys
import numpy as np
import time
start_time = time.time()

def readFile(file):
    text = open(file)
    temp = []
    for line in text:
        str = line.strip()
        temp.append(str)
    text.close()
    return temp

def main():
    arr = readFile("Day 16\input.txt")
    print(arr)


main()
print("--- %s seconds ---" % (time.time() - start_time))
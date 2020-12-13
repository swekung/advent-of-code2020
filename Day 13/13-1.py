import sys
import numpy as np
import time
start_time = time.time()

def readFile(file):
    text = open(file)
    temp = []
    for line in text:
        temp.append(line.strip())
    time = int(temp[0])
    ids = []
    for char in temp[1].split(","):
        if not "x" in char:
            ids.append(int(char))
    ids = np.array(ids)
    text.close()
    return time, ids


def findBus(time, ids):
    sinceLast = time % ids
    wait = ids - sinceLast
    index = np.argmin(wait)
    return ids[index], wait[index]

def main():
    time, ids = readFile("Day 13\input.txt")
    bus, wait = findBus(time, ids)
    print(bus * wait)


main()
print("--- %s seconds ---" % (time.time() - start_time))
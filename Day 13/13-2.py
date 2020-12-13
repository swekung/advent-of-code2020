import sys
import numpy as np
from functools import reduce
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
    ids = np.array(ids, dtype='int64')
    temp2 = temp[1].split(",")
    schedule = []
    for i in range(len(temp2)):
        if not temp2[i] == "x":
            schedule.append(i)
    schedule = np.array(schedule, dtype='int64')
    text.close()
    return time, ids, schedule

def chineseRemainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mulInv(p, n_i) * p
    return sum % prod

def mulInv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def findBus(time, ids):
    sinceLast = time % ids
    wait = ids - sinceLast
    index = np.argmin(wait)
    return ids[index], wait[index]

def main():
    time, ids, schedule = readFile("Day 13\input.txt")
    t = chineseRemainder(ids, -schedule)
    print(t)


main()
print("--- %s seconds ---" % (time.time() - start_time))
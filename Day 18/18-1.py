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
        string = string.replace(" ", "")
        temp.append(string)
    text.close()
    return temp

def compPostFix(string):
    operators = ["(", ")", "+", "*"]
    opStack = []
    outQueue = []
    for char in string[0]:
        if char not in operators:
            outQueue.append(char)
        elif char == "(":
            opStack.append(char)
        elif char == ")":
            top = opStack[-1]
            while top is not None and top !="(":
                outQueue.append(top)
                opStack.pop()
                top = opStack[-1]
            opStack.pop()
        else:
            opStack.append(char)
    while len(opStack) != 0:
        outQueue.append(opStack[-1])
        opStack.pop()
    return outQueue

def calcSum(arr):
    temp = []
    operators = ["+", "*"]
    for char in arr:
        if char not in operators:
            temp.append(int(char))
        elif char == "*":
            val1 = temp.pop()
            val2 = temp.pop()
            temp.append(val1 * val2)
        elif char == "+":
            val1 = temp.pop()
            val2 = temp.pop()
            temp.append(val1 + val2)
    return temp[0]




def main():
    arr = readFile("Day 18\itest.txt")
    sum = []
    # for line in arr:
    #     temp = compPostFix(line)
    #     sum.append(calcSum(temp))
    temp = compPostFix(arr)
    print(calcSum(temp))


main()
print("--- %s seconds ---" % (time.time() - start_time))
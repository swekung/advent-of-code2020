import sys
import re
import numpy as np
import copy
import time
start_time = time.time()

def readFile(file):
    text = open(file)
    out = []
    for line in text:
        out.append(line.strip().split())
    text.close()
    return out

def runProg(prog):
    acc = 0
    visited = np.zeros(len(prog))
    i = 0
    while True:
        if visited[i] == 1:
            return False
        else:
            visited[i] = 1
        if "acc" in prog[i][0]:
            acc += int(prog[i][1])
            i += 1
        elif "jmp" in prog[i][0]:
            i += int(prog[i][1])
        elif "nop" in prog[i][0]:
            i += 1
        if i == len(prog)-1:
            if "acc" in prog[i][0]:
                acc += int(prog[i][1])
            return True, acc
        

def debugLoop(prog):
    for i in range(len(prog)):
        debugProg = copy.deepcopy(prog)
        if "jmp" in prog[i][0]:
            debugProg[i][0] = "nop"
        elif "nop" in prog[i][0]:
            debugProg[i][0] = "jmp"
        if runProg(debugProg):
            return runProg(debugProg)
        


def main():
    instructions = readFile(("Day 8\input.txt"))
    print(debugLoop(instructions))


main()
print("--- %s seconds ---" % (time.time() - start_time))
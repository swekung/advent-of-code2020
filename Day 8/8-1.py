import sys
import re
import numpy as np
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
        if "acc" in prog[i][0]:
            acc += int(prog[i][1])
            i += 1
        elif "jmp" in prog[i][0]:
            i += int(prog[i][1])
        elif "nop" in prog[i][0]:
            i += 1
        if visited[i] == 1:
            return acc
        else:
            visited[i] = 1



def main():
    instructions = readFile(("Day 8\input.txt"))
    print(runProg(instructions))


main()
print("--- %s seconds ---" % (time.time() - start_time))
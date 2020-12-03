import sys
import time
start_time = time.time()

def readFile(file):
    text = open(file)
    out = []
    for line in text:
        line = line.strip('\n')
        out.append(list(line))
    text.close()
    return out

def findPath(map):
    i = 0
    j = 0
    count = 0
    while True:
        if map[i][j] == "#":
            count = count + 1
        i = i + 1
        j = j + 3
        if i >= len(map):
            return count
        if j >= len(map[i]):
            j = j - len(map[i])
        


def main():
    map = readFile("Day 3\input.txt")
    print(findPath(map))

main()
print("--- %s seconds ---" % (time.time() - start_time))
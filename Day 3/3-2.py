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

def findPath(map, slope):
    i = 0
    j = 0
    count = 0
    while True:
        if map[i][j] == "#":
            count = count + 1
        i = i + slope[0]
        j = j + slope[1]
        if i >= len(map):
            return count
        if j >= len(map[i]):
            j = j - len(map[i])
        
def multSlope(map, slopes):
    trees = 1
    for slope in slopes:
        trees = trees * findPath(map, slope)
    return trees

def main():
    map = readFile("Day 3\input.txt")
    slopes = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]
    print(multSlope(map, slopes))

main()
print("--- %s seconds ---" % (time.time() - start_time))
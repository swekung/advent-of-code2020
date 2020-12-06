import sys
import time
start_time = time.time()

def readFile(file):
    text = open(file)
    out = []
    for line in text:
        out.append(line.strip())
    text.close()
    return out

def findSeat(boardingpass):
    row = range(128)
    col = range(8)
    for i in range(7):
        if boardingpass[i] is "F":
            row = row[:len(row)//2]
        elif boardingpass[i] is "B":
            row = row[len(row)//2:]
    for i in range(7,10):
        if boardingpass[i] is "L":
            col = col[:len(col)//2]
        elif boardingpass[i] is "R":
            col = col[len(col)//2:]
    return row[0], col[0]
        
def findMaxSeat(arr):
    maxVal = 0
    for passport in arr:
        row, col = findSeat(passport)
        if (row * 8 + col) > maxVal:
            maxVal = row * 8 + col
    return maxVal

def main():
    file = "Day 5\input.txt"
    print(findMaxSeat(readFile(file)))

main()
print("--- %s seconds ---" % (time.time() - start_time))
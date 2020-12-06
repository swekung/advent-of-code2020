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
        
def calcAllSeats():
    rows = range(128)
    cols = range(8)
    seats = []
    for row in rows:
        for col in cols:
            seats.append(row * 8 + col)
    return seats

def notMySeat():
    rows = [0, 1, 2, 3, 122, 123, 124, 125, 126, 127]
    cols = range(8)
    seats = []
    for row in rows:
        for col in cols:
            seats.append(row * 8 + col)
    return seats

def findAllSeats(arr):
    seats = []
    for boardingpass in arr:
        row, col = findSeat(boardingpass)
        seats.append(row * 8 + col)
    return seats

def main():
    file = "Day 5\input.txt"
    boardingpasses = readFile(file)
    temp = (list(set(calcAllSeats()) - set(findAllSeats(boardingpasses))))
    temp = (list(set(temp) - set(notMySeat())))
    print(temp)

main()
print("--- %s seconds ---" % (time.time() - start_time))
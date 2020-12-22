import sys
import numpy as np
from copy import copy
import time
start_time = time.time()

def readFile(file):
    text = open(file)
    temp = []
    playerNum = 0
    for line in text:
        if "Player" in line:
            playerNum += 1
            temp.append([])
        else:
            string = line.strip()
            if not string == '':
                temp[playerNum - 1].append(int(string))
    text.close()
    return temp

def playGame(player1, player2):
    while True:
        play1 = player1.pop(0)
        play2 = player2.pop(0)
        if play1 < play2:
            player2.append(play2)
            player2.append(play1)
        else:
            player1.append(play1)
            player1.append(play2)
        if len(player1) == 0:
            return player2
        elif len(player2) == 0:
            return(player1)

def calcOut(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i] * (len(arr) - i)
    return sum

def main():
    arr = readFile("Day 22\input.txt")
    print(calcOut(playGame(arr[0], arr[1])))


main()
print("--- %s seconds ---" % (time.time() - start_time))
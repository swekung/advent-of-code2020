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


def calcOut(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i] * (len(arr) - i)
    return sum


def playGame(player1, player2):
    seen = set()
    while player1 and player2:
        state = (tuple(player1), tuple(player2))
        if state in seen:
            return player1, "1"
        else:
            seen.add(state)
            play1 = player1.pop(0)
            play2 = player2.pop(0)
            if play1 <= len(player1) and play2 <= len(player2):
                arr, winner = playGame(copy(player1[:play1]), copy(player2[:play2]))
                if winner == "1":
                    player1.append(play1)
                    player1.append(play2)
                elif winner == "2":
                    player2.append(play2)
                    player2.append(play1)
            elif play2 < play1:
                player1.append(play1)
                player1.append(play2)
            elif play1 < play2:
                player2.append(play2)
                player2.append(play1)
    return (player1, "1") if player1 else (player2, "2")
            

def main():
    arr = readFile("Day 22\input.txt")
    print(calcOut(playGame(arr[0], arr[1])[0]))


main()
print("--- %s seconds ---" % (time.time() - start_time))
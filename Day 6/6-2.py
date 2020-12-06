import sys
import numpy as np
import time
start_time = time.time()

def readFile(file):
    temp = open(file)
    text = temp.read()
    out = []
    for line in text.split("\n\n"):
        out.append(line.replace("\n", " "))
    temp.close()
    return out

def findAnswers(answers): 
    count = 0
    individual = answers.split()
    alpha = list(individual[0])
    for ans in individual:
        alpha = [value for value in ans if value in alpha]
    return len(alpha)
        
def iterAnswers(answer):
    ans = []
    for answ in answer:
        ans.append(findAnswers(answ))
    return ans

def main():
    answers = readFile("Day 6\input.txt")
    print(sum(iterAnswers(answers)))
    

main()
print("--- %s seconds ---" % (time.time() - start_time))
import sys
import re
import time
start_time = time.time()

def readFile(file):
    temp = open(file)
    text = temp.read()
    out = {}
    for line in text.split("\n"):
        line = line.split("contain")
        line[0] = line[0].strip(" ")
        line[0] = line[0].rstrip("s")
        for string in line[1].split(","):
            string = re.sub(r'\d+', '', string)
            string = string.rstrip(".")
            string = string.rstrip("s")
            string = string.strip()
            if string in out:
                tempArr = out[string]
                tempArr.append(line[0])
                out[string] = tempArr
            else:
                out[string] = [line[0]]
    temp.close()
    return out

def findBags(dict, col, input):
    out = dict[col]
    for color in out:
        try:
            if not out in input:
                out.append(findBags(dict, color, out))
        except:
            pass
    return out


def flatten(arr):
    rt = []
    res = []
    for i in arr:
        if isinstance(i,list): rt.extend(flatten(i))
        else: rt.append(i)
    for i in rt: 
        if i not in res: 
            res.append(i) 
    return res

def main():
    bags = readFile("Day 7/input.txt")
    arr = findBags(bags, "shiny gold bag", [])
    print(len(flatten(arr)))
   

main()
print("--- %s seconds ---" % (time.time() - start_time))
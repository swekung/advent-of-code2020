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
            key = re.sub(r'\d+', '', string)
            key = key.rstrip(".")
            key = key.rstrip("s")
            key = key.strip()
            if line[0].rstrip("s") in out:
                tempArr = out[line[0].rstrip("s")]
                tempArr.append([key, re.findall("\d+", string)])
                out[line[0].rstrip("s")] = tempArr
            else:
                out[line[0].rstrip("s")] = [[key, re.findall("\d+", string)]]
    temp.close()
    return out

def findBags(dict, col):
    out = dict[col]
    for color in out:
        try:
            out.append(findBags(dict, color[0]))
        except:
            pass
    return out

def countBags(dict, col):
    sum = 0
    out = dict[col[0]]
    for bag in out:
        if bag[0] == "no other bag":
            pass
        else:
            sum += int(bag[1][0]) + int(bag[1][0]) * countBags(dict, bag)
    return sum


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
    print(countBags(bags, ["shiny gold bag", 1]))
   

main()
print("--- %s seconds ---" % (time.time() - start_time))
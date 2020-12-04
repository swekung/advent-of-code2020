import sys
import time
start_time = time.time()

def readFile(file):
    temp = open(file)
    text = temp.read()
    out = []
    for line in text.split("\n\n"):
        out.append(line.strip())
    temp.close()
    return out

def countPass(arr, fields):
    count = 0
    for pa in arr:
       if all([k in pa for k in fields]):
           count += 1
    return count 

def main():
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    passports = readFile("Day 4\input.txt")
    print(countPass(passports, fields))

main()
print("--- %s seconds ---" % (time.time() - start_time))
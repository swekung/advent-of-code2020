import sys
import time
start_time = time.time()

def readFile(file):
    text = open(file)
    passwords = []
    min = []
    max = []
    char = []
    for line in text:
        line.rstrip('\n')
        for string in line.split():
            if "-" in string:
                temp = string.split("-")
                min.append(temp[0])
                max.append(temp[1])
            elif ":" in string:
                char.append(string.rstrip((":")))
            else:
                passwords.append(string)
    text.close()
    return passwords, min, max, char

def countPasswords(passwords, mins, maxs, chars):
    counter = 0
    for i in range(len(passwords)):
        password = passwords[i]
        char = chars[i]
        min = int(mins[i])
        max = int(maxs[i])
        count = password.count(char)
        if count > max or count < min:
            pass
        elif count <= max and count >= min:
            counter = counter + 1
    return counter


def main():
    passwords, min, max, char = readFile("Day 2\input.txt")
    print(countPasswords(passwords, min, max, char))

main()


print("--- %s seconds ---" % (time.time() - start_time))
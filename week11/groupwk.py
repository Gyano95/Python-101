i = 0
with open("courses.txt") as newFile:
    for line in newFile:
        i = i + 1
        cleanLine = line.strip()
        words = cleanLine.split(",")
        if i > 1:
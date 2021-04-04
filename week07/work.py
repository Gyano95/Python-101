n=int(input('Please enter a positive integer between 1 and 15: '))
number = ""

for row in range(1, n + 1):
    for col in range(1, n + 1):
        number = number + 10
        print(row*col, end="\t")
    print()
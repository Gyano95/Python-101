# List Numbers

values = []
for i in range(4):
    a = int(input("Enter value: ".format(i+1)))
    values.append(a)
    values.sort()

print("Sum is: ", sum(values))
print("Average is: ", sum(values) / len(values))
print("Maximun is: ", max(values))
print("Minimum is: ", min(values))
print("Sort list: ", values)


 
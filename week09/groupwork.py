# List Numbers
value = []
numbers = 1

while numbers != 0:
    numbers = int(input("Enter your numbers: "))
    if numbers != 0:
        value.append(numbers)

value.sort()

print("sum is: ", sum(value))
print("Average: ", sum(value)/ len(value))
print("Maximum is: ", max(value))
print("Minimum is: ", min(value))
print("The sorted list is: ")


for x in range(len(value)):
 print(value[x])   
# Example 1
employees = ["Joshus", "Tooby", "Bode"]
print(len(employees))

#***************************************************
employees = []

employees.append("John")
employees.append("Bradley")
employees.append("Junior")
employees.append("Mark")

for emploee in employees:
    print(len(employees))

#****************************************************
employees = []

new_employee = input("Who is the new employee?: ")
employees.append(new_employee)

for employee in employees:
    print(employee)

#*******************************************************
# OR

employees = []
new_employee = ""
while new_employee != "quit":
    new_employee = input("Who is the new employee?: ")
    employees.append(new_employee)

for employee in employees:
    print(employee)

#********************************************************

# EXAMPLE 2
friends = ["Betty", "John", "Bushy"]
tips = [12.25, 13.95, 8.50]

running_total = 0

for tip_amount in tips:
    # running_total = running_total + tip_amount #OR
    running_total += tip_amount

print(f"The total is: {running_total:.2f}")










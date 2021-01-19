# Area of a Square
# side = float(input('Enter is the length of a side of a square?: '))
# area = side * side
# print(f"The area of the side of a square is {area}")

# # Length of a rectangle
# length = float(input('Enter the length of rectangle?: '))
# width = float(input('Enter is the width of the rectangle?'))

# # Calculate the area
# # area = length * width

# # # output option
# print("The Area of a Rectangle using", length, "and", width, " = ", area)
# print(f'The length and width of a rectangle is: {area}')

# # Stretch 1
# # Area of a circle
# from math import pi
# r = float(input("Enter the radius of the circle : "))
# print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

# # Another output example
# radius = float(input("What is the radius of the circle? "))
# area = 3.14 * (radius ** 2)
# print(f"The area of the circle is: {area}")

# Stretch 2: Many areas from one value
# value = float(input("What is the value to be used? "))

# calculate areas

square = float(input('Enter the area square value: '))
circle = float(input('Enter the area circle: '))
square = float(input('Enter the volumn cube: '))
square = float(input('Enter the volumn spere: '))

# Function
from math import pi
area_square = value ** 2
area_circle = 3.14 * (value ** 2)
volume_cube = value ** 3
volume_sphere = (4 / 3) * 3.14 * (value ** 3)

#  display results
print(f"Area of a square: {area_square}")
print(f"Area of a circle: {area_circle}")
print(f"Volume of a cube: {volume_cube}")
print(f"Volume of a sphere: {int(volume_sphere)}")

# Area of a rectangle
length = float(input("What is the length of rectangle (in cm)? "))
width = float(input("What is the width of the rectangle (in cm)? "))
area = length * width
print(f"The area of the rectangle is: {area} cm^2")
print(f"The area of the rectangle is: {area / 10000} 

# Area of a circle
radius = float(input("What is the radius of the circle (in cm)? "))
area = 3.14 * (radius ** 2)
print(f"The area of the circle is: {area} cm^2")
print(f"The area of the circle is: {area / 10000} m^2")
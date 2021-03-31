from math import pi

def areaSquare( side ):
    area = side * side
    return area

def areaRectangle(a, b):
    return (a * b)

def perimeterRectangle(a, b):
    return (2 * (a + b))

side = int(input("What is the sided of Area Square?: "))
print("Area of Square is: ", areaSquare(side))
print("\n")

a = int(input("What is the Area of a Rectangle?: "))
b = int(input("What is the Parameter of Rectangle?: "))
print("Area of Rectangle = ", areaRectangle(a, b))
print ("Perimeter of a Rectangle = ", perimeterRectangle(a, b))
print("\n")

r = float(input ("Input the radius of the circle: "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))
    

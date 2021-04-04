from math import pi

def areaSquare( side ):
    area = side * side
    return area

def areaCircle(radius):
    return str(pi * radius ** 2)

def areaRectangle(a, b):
    return (a * b)

def compute_area(shape, side1, side2=0):
    area = -1

    if shape == "square":
        area = areaSquare(side)
    elif shape == "circle":
        area == areaCircle(side)
    elif shape == "rectangle":
        area = areaRectangle(a, b)

    return area

shape = " "

while shape != "quit":
    shape = input("What shape do you have? ")
    shape = shape.lower()

    if shape == "square":
        side = int(input("What is the sided of Area of a Square?: "))
        print("Area of Square is: ", areaSquare(side))
        print("\n")
    elif shape == "circle":
            r = float(input ("Input the radius of the circle: "))
            print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))
            print("\n")
    elif shape == "rectangle":
        a = int(input("What is the length of a Rectangle?: "))
        b = int(input("What is the Parameter of Rectangle?: "))
        print("Area of Rectangle = ", areaRectangle(a, b))
        print(quit)



# Unit Conversion

# fahrenheit = float(input('Temp in fahrenheit: '))
# celsius = (fahrenheit - 32) * 5/9
# print(f'Fahrenheit is: {celsius:.2f}')

# print('%.1f Fahrenheit is: %0.1f Celsius' %(fahrenheit, celsius))



# Speed of a Falling Object

import math
print('Welcome to the velocity calculator. Please enter the following: ')
print(f'\n')

m = float(input("Mass (in kg): "))
g = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
t = float(input("Time (in seconds): "))
p = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
A = float(input("Cross sectional area (in m^2): "))
C = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

# First calculate c = 1/2 p A C
c = (1 / 2) * p * A * C

# Now calculate the velocity v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)*t))
v = math.sqrt(m * g / c) * (1 - math.exp((-math.sqrt(m * g * c) / m) * t))

print() # display a blank line
print(f"The inner value of c is: {c:.3f}")
print(f"The velocity after {t} seconds is: {v:.3f} m/s")




# weight = int(input("What is your weight in pounds?"))
# mass = weight / 2.2
# mass_rounded = round(mass,0)

# print("Your mass is:", int(mass_rounded), "kg.")









# print(f'v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)t))')


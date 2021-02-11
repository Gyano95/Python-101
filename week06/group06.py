# # Amusement Park Rides
can_ride = False

age1 = input("What is your age?: ")
height1 = input("What is your height?: ")

second_rider = input("Is there a second  (yes or no)?: ")

if second_rider.lower() == "yes":
    age2 = int(input("Second rider's age is?: "))
    height2 = int(input("Second driver's height is?: "))

    if height1 < 36 or height2 < 36:
        can_ride = False
    else:
        # Rule 3
        if age1 >= 18 or age2 >= 18:
            # At least one is an adult
            can_ride = True
        else:
            can_ride = False
else:
    if age1 >= 18 and height1 >= 62:
        can_ride = True
    else:
        can_ride = False
if  can_ride:
    print("Welcome")
else:
    print("Sorry you can't ride")
 

# can_ride = False

# age1 = int(input("What is the age of the first rider? "))
# height1 = int(input("What is the height of the first rider? "))

# is_second_rider = input("Is there a second rider (yes/no)? ")

# if is_second_rider.lower() == "yes":
#     age2 = int(input("What is the age of the second rider? "))
#     height2 = int(input("What is the height of the second rider? "))

#     # Rule 1
#     if height1 < 36 or height2 < 36:
#         can_ride = False
#     else:
#         # Rule 3
#         if age1 >= 18 or age2 >= 18:
#             # At least one is an adult
#             can_ride = True
#         else:
#             # Neither is an adult
#             can_ride = False
# else: # There is only one rider
#     # Rule 2
#     if age1 >= 18 and height1 >= 62:
#         can_ride = True
#     else:
#         can_ride = False

# if can_ride:
#     print("Welcome to the ride. Please be safe and have fun!")
# else:
#     print("Sorry, you may not ride.")
# # If Statement

user1 = int(input('Enter number? '))
user2 = int(input('Enter number? '))

if user1 > user2:
    print('User1 is grather')
else:
    print('User1 is not greater')

if user1 == user2:
    print('Numbers are equal')
else:
    print('Numbers are not equal')
    
if user2 > user1:
    print('User2 is greater')
else:
    print('User2 is not greater')

print() # Blank line

# Favourite Animal
animal = input("What is your favorite animal? ")

if animal.lower() == "zebra":
    print("That's my favorite animal too!.")
else: 
    print('That one is not my favorite.')    
  
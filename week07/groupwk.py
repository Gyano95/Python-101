# guess = ""
# response = ""

# guess1 = input("What is your lucky number: ")
# guess2 = input("What is your guess: ")

# while guess == 10:
#     print(f'Higher')
#     if response > 10:
#         print(f'Lower')
 
# print("Thank you for playing. Goodbye.")

number = 0
guess = ""
while number < 1:
    number = int(input("What is the number? "))
    guess = int(input("What is your guess?: "))
    print(f"Lower")
    number = int(input("What is the number? "))
    guess = int(input("What is your guess?: "))
if guess > 1:
    print(f"Higher")

print("Finished with the loop")
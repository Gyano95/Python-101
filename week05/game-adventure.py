#**********Milestone - Adventure Game**********
yes_no = {"yes", "no"}
directions = {"left", "forward", "backward"}

name = input("Choose an adventure name: ")
print(f'\n')
print(f"Hey, {name} Let's go on adventure!")
print("Becareful what you wish for in this game, but nothing to be afarid of!\n")

print("You find yourself at the edge of a cliff!.")
print("What do you do?\n")

# Game start
response = " "
while response not in yes_no:
    response = input("Would you jump?: ")
    if response.lower() == "yes":
        print(f"You are brave {name}, person like you are goal getter!\n")
    elif response.lower() == "no":
        print(f"Common {name}, incase you changed your mind. ")
        print("Start again!")
        quit()
else:
    print(f"I do not get that {name}!")

print(f'\n')

response = " "
while response not in directions:
    print("Because you believe you can fly, then you did and landed safely.")
    print("To your right, there is a river full of crocodile, almost the way out.")
    print("To your left, is a thick forest leading to unknown.")
    print("Your backward, you can't even imagine to risk that.")
    print("But you can continue to believe in yourself\n")
    response = input("What direction do you move?\n left/forward/backward\n")

    if response.lower() == "backward":
        print(f"Sorry {name}, you just turn to a pillar of salt!") 
        quit()
    elif response.lower() == "left":
        print(f"Sorry {name}, you should have a good choice next time!")
        quit()
    elif response.lower() == "forward":
        print(f"You are such a brave {name}, those are not crocodile!. They are  river-rock leading you to your desire destination. 'Prophet Jeffrey R.Holland 'No one has failed who keeps trying and keep praying'. Congratulation!")
    
    else:
        print("I don't get it")









# Checkpoint Examples
members = []

new_member = ""
while new_member != "end":
    new_member = input("What is the name of our new members?: ")
    members.append(new_member)

for member in members:
        print(f"New members are: {member}")

        
        # TUTOR EXAMPLE
        # Purpose: Practice using lists, by adding the names of friends.

# First, I'm going to set up an empty list called, friends.
# Notice that I call it friends (with an s) not friend. This will help me
# remember throughout my code that it is a list of potentially many friends
# rather than a single friend.
friends = []

# This will be used in my loop to get the name of each friend that I want
# to put in the list. I can start it will any value, as long as that value
# is not "end", otherwise, it won't ever go into the loop I made to gather
# the names.
name = None

while name != "end":
    name = input("Type the name of a friend: ")

    # Without this if statement, I would put "end" into my list as well
    if name != "end":
        friends.append(name)

print()
print("Your friends are:")

for friend in friends:
    print(friend)


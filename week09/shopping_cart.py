# SHOPPING CART!
prices = []
items = []
quantity = []

prompt_user = """
Welcom2 to our Shop, please choose an option:
1 - Add new item
2 - Display the contents of the shopping cart
3 - Remove an item (only needed for the final project deliverable)
4 - Compute the total (only needed for the final project deliverable)
5 - Quit\n
"""

response = 0

while response != 5:
    response = int(input(prompt_user))
    if response == 1:
        x = input("What item would you like to add?")
        qnty = int(input("How many?: "))
        y = float(input(f"What is the price of the {x}: "))
        print(f"Adding {x.upper()} to your cart\n...Please wait...")
        items.append(x.title().upper().strip())
        y = y * qnty
        quantity.append(qnty)
        prices.append(y)   

    elif response == 2: 
        for price, item, qnty in zip(prices, items, quantity):
            print(f"Total cost: ${price:.2f}, Item name: {item}, Quantity: {qnty}")
        input("\nPlease press ENTER to continue.")

    elif response == 3:
        for price, item, qnty in zip(prices, items, quantity):
            print(f"Total cost: ${price:.2f}, Item name: {item}, Quantity: {qnty}")
        delete_item = input(
            "\nType the item would you like to remove? ").title()
        qnty = int(input("How many item would you want to remove?: "))
        
        print("Deleting item\n...Please wait...")
        idx_num = items.index(delete_item.upper().strip())
        if quantity[idx_num] - qnty < 0:
            print(f"Error, please select the correct number of items!")
        elif quantity[idx_num] - qnty == 0:
            
            items.pop(idx_num)
            quantity.pop(idx_num)
            prices.pop(idx_num)
            for price, item in zip(prices, items):
                print(f"{price:.2f}\t{item}")
        elif quantity[idx_num] - qnty > 0:
            prices[idx_num] = prices[idx_num] - qnty * (prices[idx_num] / quantity[idx_num])
            quantity[idx_num] = quantity[idx_num] - qnty
        input("\nPlease press Enter to continue.")

    elif response == 4:
        for price, item, qnty in zip(prices, items, quantity):
            print(f"Total cost: ${price:.2f}, Item name: {item}, Quantity: {qnty}")
        print(f"\nYour total cart value is ${sum(prices):.2f}")
        input("\nPlease press Enter to continue.")
        
print("\nThank you. Goodbye!\n")
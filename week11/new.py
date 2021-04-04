shopping_cart = [
    ["Chips", 2.99],
    ["Bread", 2.50],
    ["Milk", 3.19],
    ["Ice Cream", 6.99],
    ["Cheese", 5.99],
    ["Candy bar", 0.99]
]

max_price = -1

for item in shopping_cart:
    price = item[1] # The price is the second part of the item

    if price > max_price:
        # This is the new max
        max_price = price

print(f"The maximum price is: {max_price}")


max_price = -1
max_product = "" # It doesn't matter what you set this to, it just needs to be declared

for item in shopping_cart:
    product_name = item[0] # Product name is the first part
    price = item[1] 

    if price > max_price:
        # This is the new max
        max_price = price

        # Also save this product name as the max product
        max_product = product_name

print(f"The maximum price is: {max_price}")
print(f"The product with the maximum price is: {max_product}")
with open("hr_system.txt") as f:
    # The file has now been opened and stored in a variable "f"

    # Read each line, one by one, into a variable: current_line
    for line in f:
        # Split the current line into its parts based on a space " " as the separator
        parts = line.split(" ")

        # Save the parts we need into variables
        name = parts[0]
        id_number = parts[1]
        title = parts[2]
        salary = float(parts[3])

        # Output the name and title as desired
        print(f"Name: {name}, (ID: {id_number}), Title: {title}, Salary: ${salary}")

        # pay_amount = salary / 24
        # if title.lower() == "engineer":
        #     pay_amount +- 1000

        # print(f"{name} (ID: {id_number}), {title} - ${pay_amount:.2f}")

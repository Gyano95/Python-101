# Variables and Expression

child_meal = float(input("Price of child's meal? "))
adult_meal = float(input("Price of adult's meal? "))
children = int(input("Number of children? "))
adult = int(input("Number of adult? "))
sale_tax_rate = float(input("sale tax rate: "))
print(f'\n')

# Calculate
subtotal = children * child_meal + adult * adult_meal
print('Subtotal: ${:.2f}'.format(subtotal))

sale_tax = subtotal * sale_tax_rate / 100
print('sale tax: ${:.2f}'.format(sale_tax))

total_price = subtotal + sale_tax
print('Total: ${:.2f}'.format(total_price))
print(f'\n')

# Payment amount and change
total_amount = float(input("Total meal payment amount? "))
change = total_amount - total_price

print('Your change is: ${:.2f}'.format(change))
print(f'\n')

change_tip = input('buyer: Keep the change - click for response')

print('Seller: Thank you for the tips!')


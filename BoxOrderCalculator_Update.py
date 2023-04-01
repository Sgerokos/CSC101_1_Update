# Import the math library
import math

# Ask the user to enter the number of boxes they want to buy
while True:
    try:
        quantity = int(input("Please enter the number of boxes to buy (max 200): "))
        if quantity <= 0 or quantity > 200:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 200.")

# Calculate the total cost
amount = quantity * 1.50

# Ask the user for the shipping location
shipping = input("Please enter a shipping location (NY or other): ")

# If shipping is NY, add 8.75% for taxes
if shipping == "NY":
    amount += amount * 0.0875

# Apply discount if quantity is greater than 50
if quantity > 50:
    amount *= 0.8

# Ask the user for the shipping mode
shipping_mode = input("What type of shipping mode would you like? Please enter Air or Ground: ")

# Estimate the price of the shipping mode
if shipping_mode == "Air":
    amount += 50
else:
    amount += 10

# Print the total amount
print("The total amount is: $" + str(round(amount, 2)))
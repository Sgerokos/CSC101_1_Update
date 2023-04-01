# Import the time library
import time

# Ask the user for the investment amount
investment_amount = float(input("Please enter the investment amount: "))

# Ask the user for the annual interest rate
annual_interest_rate = float(input("Please enter the annual interest rate as a decimal: "))

# Ask the user for the number of years to invest
num_years = int(input("Please enter the number of years to invest: "))

# Calculate the future investment value using the formula
future_investment_value = investment_amount * (1 + (annual_interest_rate / 12)) ** (num_years * 12)

# Round the result to 2 decimal places and print it to the user
print("The accumulated value is:", round(future_investment_value, 2))
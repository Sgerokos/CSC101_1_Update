# Import the time library
import time

# Ask the user for the investment amount, annual interest rate, and number of years to invest
investment_amount = float(input("Please enter the investment amount: "))
annual_interest_rate = float(input("Please enter the annual interest rate as a decimal: "))
num_years = int(input("Please enter the number of years to invest: "))

# Validate the user's input
if investment_amount < 0 or annual_interest_rate < 0 or num_years < 0:
    print("Invalid input. Please enter non-negative values.")
else:
    # Calculate the future investment value using the compound interest formula
    # FV = P * (1 + r/n)^(n*t), where:
    # FV = future investment value
    # P = investment amount
    # r = annual interest rate
    # n = number of times compounded per year (default is 12)
    # t = number of years invested
    n = 12  # Default compounding frequency is monthly
    future_investment_value = investment_amount * (1 + (annual_interest_rate / n)) ** (n * num_years)

    # Format and print the result to the user
    formatted_result = "${:,.2f} after {} years of investing at an annual interest rate of {}%"
    print("The accumulated value is:", formatted_result.format(future_investment_value, num_years, annual_interest_rate*100))
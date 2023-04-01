# Import the math library for trigonometric functions
import math

# Ask the user for the number of sides
number = int(input("Please enter the number of sides: "))

# Ask the user for the length of the sides
side_length = float(input("Please enter the length of the sides: "))

# Calculate the area using the number of sides and side length
area = number * side_length ** 2 / (4 * math.tan(math.pi / number))

# Print the area on screen for the user
print("The area of the polygon is {:.2f}".format(area))
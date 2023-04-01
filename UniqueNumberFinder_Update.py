# Ask the user to enter 10 numbers separated by spaces
n = input("Please enter 10 numbers: ")

# Extract the numbers from the input and convert them to integers
n = n.split()
if len(n) != 10:
    print("Error: you must enter exactly 10 numbers")
    exit()
n = [int(num) for num in n]

# Create a new list containing only the unique numbers
unique_numbers = []
for i in n:
    if i not in unique_numbers:
        unique_numbers.append(i)

# Display the unique numbers
print("The numbers are: ", end="")
for i in range(len(unique_numbers)):
    print(unique_numbers[i], end=" ")
print()
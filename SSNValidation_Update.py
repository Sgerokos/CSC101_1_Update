# Asks the user to enter a social security number
SSN = input("Please enter a Social Security Number: ")

# Variable to verify the number
is_valid_ssn = True

# Check if the SSN is valid
if len(SSN) != 11:
    # If length is not 11, it is invalid
    is_valid_ssn = False
elif SSN[3] != "-" or SSN[6] != "-":
    # If the dashes are not at the correct places, it is invalid
    is_valid_ssn = False
elif not (SSN[:3].isdigit() and SSN[4:6].isdigit() and SSN[7:].isdigit()):
    # If the numeric parts do not consist of numbers, it is invalid
    is_valid_ssn = False

# Print the result
if is_valid_ssn:
    print(f"{SSN} is a valid SSN")
else:
    print(f"{SSN} is an invalid SSN")
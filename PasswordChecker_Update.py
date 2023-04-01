# This program checks if a password is valid based on certain requirements.

def checkPassword(password):
    """
    Checks if a password is valid based on the following requirements:
    - At least 8 characters
    - At least 2 digits
    - A mix of letters and digits
    
    Parameters:
    password (str): the password to check
    
    Returns:
    bool: True if the password is valid, False otherwise
    """
    count_letters = 0
    count_digits = 0

    # Iterate through each character in the password
    for ch in password:
        # If the character is a digit, increment count_digits
        if ch.isdigit():
            count_digits += 1
        # If the character is alphabetic, increment count_letters
        elif ch.isalpha():
            count_letters += 1
        # If the character is anything else, the password is invalid
        else:
            return False

    # If the password meets the criteria, return True
    if (count_digits >= 2 and count_letters + count_digits >= 8):
        return True 
    else:
        return False


def main():
    # Ask the user to enter a password
    password = input("Please enter your password: ")

    # Check if the password is valid and print a message
    if password and checkPassword(password):
        print("Valid password")
    else:
        print("Invalid password. The password must be at least 8 characters long with at least 2 digits and a mix of letters and digits.")


# Call the main function
main()
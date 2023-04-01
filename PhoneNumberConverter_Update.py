# Return the number associated with an alphabet
def get_num(uppercase_letter):
    num_map = (("A","B","C"),("D","E","F"),("G","H","I"),("J","K","L"),
               ("M","N","O"),("P","Q","R","S"),("T","U","V"),("W","X","Y","Z"))

    # Loop through each inner tuple
    for num in num_map:
        # Loop through each alphabet in inner tuple
        for letter in num:
            # Check if alphabet is equal to alphabet passed
            if letter == uppercase_letter:
                # Return the associated number
                return num_map.index(num) + 2

# Get the new phone number
def letter_to_num(word):
    # Get numbers associated with letters using list comprehension
    phone_number = "".join([str(get_num(letter.upper())) for letter in word])
    return phone_number

def main():
    # Ask the user to input a phone number with or without dashes, then read the input and split
    phone_num = input("Please enter a phone number with or without dashes: ").split("-")

    # Look to see if it contains the symbol
    if len(phone_num) == 3:
        # Format the phone number with dashes
        area_code, exchange_code, remaining_digits = phone_num
        phone_number = f"{area_code}-{exchange_code}-{letter_to_num(remaining_digits)}"
    else:
        # Format the phone number without dashes
        phone_number = f"{phone_num[0][:4]}{letter_to_num(phone_num[0][4:])}"

    print(phone_number)

if __name__ == "__main__":
    main()
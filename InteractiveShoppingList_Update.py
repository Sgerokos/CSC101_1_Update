# Define functions to add, remove, find, print, and quit the list

def add_item(my_list):
    """Add an item to the list."""
    item = input("Please enter the item to add to the list: ")
    my_list.append(item)

def remove_item(my_list):
    """Remove an item from the list."""
    item = input("Please enter the item to remove from the list: ")
    try:
        my_list.remove(item)
    except ValueError:
        print(item + " is not on the list.")

def find_item(my_list):
    """Find an item in the list."""
    item = input("What item would you like to find in the list? ")
    try:
        index = my_list.index(item)
        print(item + " found on the list at index " + str(index + 1) + ".")
    except ValueError:
        print(item + " is not on the list.")

def print_list(my_list):
    """Print the items in the list."""
    if len(my_list) == 0:
        print("The list is empty.")
    else:
        print("List of items:")
        for i, item in enumerate(my_list):
            print(str(i + 1) + ". " + item)

def main():
    # Create an empty list
    my_list = []

    # Display a welcome message
    print("Welcome to the list program!")
    
    # Sentinal controlled loop
    while True:
        # Ask the user for their input
        user_input = input("\nMenu: A)dd, R)emove, F)ind, P)rint, Q)uit: ")
        
        # Add an item to the list
        if user_input == "A":
            add_item(my_list)
            
        # Remove an item from the list
        elif user_input == "R":
            remove_item(my_list)
            
        # Find an item in the list
        elif user_input == "F":
            find_item(my_list)
            
        # Print the items in the list
        elif user_input == "P":
            print_list(my_list)
            
        # Quit the program
        elif user_input == "Q":
            print("Thank you for using the list program!")
            break
        
        # Handle invalid input
        else:
            print("Invalid input. Please try again.")
    
if __name__ == "__main__":
    main()
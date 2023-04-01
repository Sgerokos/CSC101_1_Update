# Import's random module
import random

user_wins = 0
computer_wins = 0

while user_wins <= 2 and computer_wins <= 2:
    # Ask the user to choose one number from the given list and generate one number randomly for the computer
    user_choice = int(input("scissors (0), rock (1), paper (2): "))

    if user_choice not in [0, 1, 2]:
        print("Invalid choice. Please choose again.")
        continue

    computer_choice = random.randint(0, 2)

    # Check who wins and increase the variable for user wins and computer wins if both are the same it is a draw and won't increase for either
    if user_choice == 0 and computer_choice == 1:
        print("The computer is rock. You are scissors. You lost. Sorry.")
        computer_wins += 1
    elif user_choice == 1 and computer_choice == 0:
        print("The computer is scissors. You are rock. You win. Congratulations!")
        user_wins += 1
    elif user_choice == 1 and computer_choice == 2:
        print("The computer is paper. You are rock. You lost. Sorry.")
        computer_wins += 1
    elif user_choice == 2 and computer_choice == 1:
        print("The computer is rock. You are paper. You win. Congratulations!")
        user_wins += 1
    elif user_choice == 2 and computer_choice == 0:
        print("The computer is scissors. You are paper. You lost. Sorry.")
        computer_wins += 1
    elif user_choice == 0 and computer_choice == 2:
        print("The computer is paper. You are scissors. You win. Congratulations!")
        user_wins += 1
    elif user_choice == computer_choice == 0:
        print("The computer is scissors. You are scissors. It is a draw.")
    elif user_choice == computer_choice == 1:
        print("The computer is rock. You are rock. It is a draw.")
    else:
        print("The computer is paper. You are paper. It is a draw.")

    # Print the number of wins for user and computer
    print(f"The computer has won {computer_wins} times.")
    print(f"You have won {user_wins} times.")

    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() == "n":
        break
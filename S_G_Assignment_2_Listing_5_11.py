# Ask the user to enter the number of students
num_students = int(input("Please enter the number of students: "))

# Initialize the highest and second highest scores
highest_score = 0
second_highest_score = 0

# Ask the user for the scores of each student and update the highest and second highest scores
for i in range(num_students):
    while True:
        try:
            score = int(input(f"Please enter the score for student {i+1}: "))
            if score < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a non-negative integer.")
    if score > highest_score:
        second_highest_score = highest_score
        highest_score = score
    elif score > second_highest_score:
        second_highest_score = score

# Display the highest and second highest scores to the user
print(f"The highest score is {highest_score}.")
print(f"The second highest score is {second_highest_score}.")
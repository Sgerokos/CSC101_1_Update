# Import's the random module
import random

# Import's the time module
import time

# Count's the number of correct answers
num_correct = 0 

# Count's the number of incorrect answers
num_incorrect = 0 

# The longest streak of correct answers
longest_streak = 0 

# The current streak of correct answers
current_streak = 0 

# The maximum number of incorrect answers before the quiz ends
max_incorrect = 3 

# Start the quiz
start_time = time.time() 

for _ in range(100):
    # Generate two random integers
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    # Swap num1 and num2 if num1 is less than num2
    if num1 < num2:
        num1, num2 = num2, num1

    # Prompt the user to answer num1 - num2
    try:
        answer = int(input(f"What is {num1} - {num2}? Enter -1 to quit. "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    
    if answer == -1:
        break

    # Check if the answer is correct and display the result
    if num1 - num2 == answer:
        print("Your answer is correct!")
        num_correct += 1 
        is_correct = True 
    else:
        print(f"Your answer is incorrect. {num1} - {num2} is {num1 - num2}")
        num_incorrect += 1  
        is_correct = False
    
    # Update streaks
    if is_correct:
        current_streak += 1 
        if current_streak > longest_streak:
            longest_streak = current_streak
    else:
        current_streak = 0 

    # Check if the quiz should end
    if num_incorrect == max_incorrect:
        print(f"You have reached {max_incorrect} incorrect answers. The quiz ends now.")
        break 

# Calculate the total score and test time
end_time = time.time() 
test_time = int(end_time - start_time)
total_score = num_correct + (longest_streak * 10)

# Print results for the user
print(f"\nThe total score is {total_score}")
print(f"Total correct answers: {num_correct}")
print(f"Total incorrect answers: {num_incorrect}")
print(f"The longest streak of correct answers: {longest_streak}")
print(f"The duration of the test: {test_time} seconds")
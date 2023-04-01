# Ask the user to input the name and grades of the student
student_input = input("Please enter the student's name followed by the grades (separated by commas): ")

# Split the grades into a list
grades_list = student_input.split(",")

# Make sure the input has exactly 6 elements (name + 5 grades)
if len(grades_list) != 6:
    print("Invalid input! Please enter the student's name followed by 5 grades.")
else:
    # Extract the grades and convert them to integers
    student_grades = [int(grade) for grade in grades_list[1:]]

    # Compute the total grade
    total_grade = sum(student_grades)

    # Calculate the letter grade based on the total grade
    if total_grade >= 90:
        letter_grade = "A"
    elif total_grade >= 80:
        letter_grade = "B"
    elif total_grade >= 70:
        letter_grade = "C"
    elif total_grade >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    # Print the student's name, grades, and letter grade
    print("{}'s grades: {}, {}, {}, {}, {}. Letter grade: {}".format(
        grades_list[0], student_grades[0], student_grades[1],
        student_grades[2], student_grades[3], student_grades[4],
        letter_grade))
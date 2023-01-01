# Dictionary to map grades to their corresponding values
grade_values = {
    "A+": 4.0,
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D+": 1.3,
    "D": 1.0,
    "D-": 0.7,
    "F": 0
}

# Prompt the user to enter the number of subjects
num_subjects = int(input("Enter the number of subjects: "))

# Initialize variables to store the total GPA and the number of subjects
total_gpa = 0
count = 0

# Loop through each subject
while count < num_subjects:
    # Prompt the user to enter the name of the course and the grade
    course = input("Enter the name of the course: ")
    grade = input("Enter the grade: ")

    # Convert the grade to uppercase to make it non-case sensitive
    grade = grade.upper()

    # Check if the grade is valid
    if grade not in grade_values:
        print("Invalid grade. Please enter a valid grade.")
        continue

    # Print the course and grade
    print(f"({course.capitalize()}: {grade})")

    # Prompt the user to confirm the entry
    confirmation = input("Is this entry correct? (yes/no) ")
    if confirmation.lower() != "yes":
        continue

    # Add the GPA value of the grade to the total GPA
    total_gpa += grade_values[grade]
    count += 1

# Calculate the average GPA
average_gpa = total_gpa / count

# Print the average GPA
print(f"Average GPA: {average_gpa:.2f}")
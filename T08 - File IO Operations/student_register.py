# Exam Registration Program

# Program Intro
print("Welcome to the exam register program!")

# Establish student ID list
student_id_list = []

# Prompt user for number of students taking part in exam
num_of_students = int(input("Enter the number of students registering for this exam: "))

# Using while loop; append list with ID numbers from user prompts
while len(student_id_list) != num_of_students:
    student_id = input("Enter the student's ID number: ")
    # Add student ID and placeholder for student name
    student_id_list.append(f"Student ID Number: {student_id.ljust(10)}Student Name: {'_' * 20}\n")

# Join list into string variable for writing to reg_form.txt
formatted_student_id_list = "".join(student_id_list)

# Write student ID list into reg_form.txt
with open('reg_form.txt', 'w+') as file:
    file.write(formatted_student_id_list)

# Read from the file and print its content, to confirm code works
with open('reg_form.txt', 'r') as file:
    contents = file.read()
    print("Contents of the file:")
    print(contents)

# Summary of the script functionality
"""
This script allows the user to register students for an exam venue by entering their
ID numbers. It prompts for the number of students, collects ID numbers in a loop,
formats them with placeholder names, writes them to 'reg_form.txt', and then reads
and displays the contents of the file to confirm successful writing.
"""

# Conclusion
"""
The script effectively demonstrates file writing and reading operations in Python.
It uses a while loop for iterative data input, string formatting techniques, and
file handling methods to manage data persistence. The program confirms its correct
functionality by displaying the contents of the written file to the user.
"""

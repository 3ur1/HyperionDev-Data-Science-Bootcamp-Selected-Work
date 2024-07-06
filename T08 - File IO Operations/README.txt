Python File IO Operations

Overview
--------

This repository contains two Python scripts demonstrating file input/output operations:

1. DOB Task (dob_task.py):
   - This script reads data from the 'DOB.txt' file and prints out names and birthdates in separate sections.
   - It processes each line from the file to extract and format names and birthdates accordingly.

2. Exam Registration Program (exam_register.py):
   - This script allows users to register students for an exam venue by entering their ID numbers.
   - It prompts for the number of students, collects ID numbers using a while loop, formats them with placeholder names, writes them to 'reg_form.txt', and then reads and displays the contents of the file to confirm successful writing.

Usage
-----

DOB Task (dob_task.py)
-----------------------

1. File Requirement:
   - Ensure the 'DOB.txt' file is placed in the same directory as 'dob_task.py'.

2. Running the Script:
   - Execute dob_task.py in your Python environment.
   - The script will read 'DOB.txt', extract names and birthdates, and display them in separate sections.

Exam Registration Program (exam_register.py)
--------------------------------------------

1. Running the Script:
   - Execute exam_register.py in your Python environment.
   - Follow the prompts to enter the number of students and their respective ID numbers.
   - The script will format the student IDs, write them to 'reg_form.txt', and then display the contents of the file to confirm successful writing.

Notes
-----

- Both scripts demonstrate basic file handling operations in Python.
- Ensure all files ('DOB.txt', 'dob_task.py', and 'exam_register.py') are located in the same directory for the scripts to execute correctly.

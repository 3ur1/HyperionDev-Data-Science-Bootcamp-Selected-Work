# dob_task.py

import os

def read_dob_file(file_path):
    """
    Reads data from the provided file path, extracts names and birthdates,
    and prints them in separate sections.

    Args:
    - file_path (str): Path to the file containing names and birthdates.

    Returns:
    - None
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

            # Initialize lists to store names and birthdates
            name_list = []
            birthdate_list = []

            # Process each line in the file
            for line in lines:
                words = line.split()
                # Extract name and birthdate
                name = ' '.join(words[:2])
                birthdate = ' '.join(words[-3:])
                # Append to respective lists
                name_list.append(name)
                birthdate_list.append(birthdate)

            # Convert lists to formatted strings with line breaks
            names_string = '\n'.join(name_list)
            birthdates_string = '\n'.join(birthdate_list)

            # ANSI escape code for formatting
            BOLD = '\033[1m'
            UNDERLINE = '\033[4m'
            RESET = '\033[0m'

            # Print names section
            print(BOLD + UNDERLINE + 'Name' + RESET)
            print(names_string)

            # Print a newline for spacing
            print()

            # Print birthdates section
            print(BOLD + UNDERLINE + 'Birthdate' + RESET)
            print(birthdates_string)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

# Summary of the script functionality
"""
This script reads data from a text file containing names and birthdates,
and prints them in two sections: 'Name' and 'Birthdate'. It utilizes
file handling to read the data, processes each line to extract relevant
information, and formats the output for display.
"""

# Conclusion
"""
The script effectively demonstrates file reading operations in Python,
uses list manipulation to organize data, and employs ANSI escape codes
for basic text formatting. Error handling is included to manage cases
where the specified file path is incorrect or the file is missing.
"""

if __name__ == "__main__":
    # Assuming DOB.txt is in the same directory as this script
    file_path = os.path.join(os.path.dirname(__file__), 'DOB.txt')
    read_dob_file(file_path)

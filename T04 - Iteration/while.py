# Iteration Practical Task 1
# This script continually asks the user to enter numbers until -1 is entered.
# It calculates and prints the average of the entered numbers, excluding -1.

def calculate_average():
    """
    This function continuously asks the user to enter numbers until -1 is entered.
    It then calculates and prints the average of the entered numbers, excluding the -1.
    """
    # Initialize variables to keep track of running total and count of numbers entered
    running_total = 0
    count = 0

    while True:
        try:
            # Prompt the user to enter a number
            number_loop = int(input("Please enter a number (-1 to stop): "))
            
            # Check if the entered number is -1 to stop the loop
            if number_loop == -1:
                break
            
            # Add the entered number to the running total
            running_total += number_loop
            # Increment the count of numbers entered
            count += 1
        
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Check if any valid numbers were entered
    if count > 0:
        # Calculate the average of the entered numbers
        average = running_total / count
        # Print the average to the user
        print("Here's your average:", average)
    else:
        # If no valid numbers were entered, inform the user
        print("No valid numbers were entered to calculate an average.")

if __name__ == "__main__":
    calculate_average()

# Conclusion
# This script effectively utilizes a while loop to handle user input until termination.
# It calculates the average of valid inputs, excluding -1, and incorporates error handling for invalid inputs.
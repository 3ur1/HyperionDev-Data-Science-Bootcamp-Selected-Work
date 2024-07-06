# Iteration - Practical Task 2
# This script prints a specific pattern using a single for loop and if-else statements.

def print_pattern():
    """
    This function prints the following pattern using a single for loop and if-else statements:
    *
    **
    ***
    ****
    *****
    ****
    ***
    **
    *
    """
    print("This is a program for printing a pattern.")

    star = '*'  # Define the star character

    print("Observe the pattern below:")

    # First half of the pattern
    for row in range(1, 6):
        print(star * row)

    # Second half of the pattern
    for row in range(4, 0, -1):
        print(star * row)

if __name__ == "__main__":
    print_pattern()

# Conclusion
# This script uses a single for loop and if-else statements to print a specific pattern.
# It demonstrates control flow in Python and could be further optimized using list comprehensions.

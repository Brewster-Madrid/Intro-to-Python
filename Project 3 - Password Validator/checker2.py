""" In this version, we will build upon the first program by adding more features.
The user will be asked to enter their username before entering their password.
The user will be given the option to hide or show their password while typing."""

# Import the getpass module to allow password input without displaying it on the screen.
# Import the string module to access predefined sets of characters such as digits, letters, and punctuation.

# Define a function to check if the password contains at least one punctuation character.
# Loop through each character in the password.
# If any character is found in the set of punctuation marks, return True.
# Otherwise, return False.

# Define a function to check if the password contains at least one numeric digit.
# Loop through each character in the password.
# If any character is a digit (0-9), return True.
# Otherwise, return False.

# Define a function to check if the password contains at least one letter (uppercase or lowercase).
# Loop through each character in the password.
# If any character is an alphabetic letter, return True.
# Otherwise, return False.

# Define the main function to check the strength of the password.
# Prompt the user to enter their username.

# Check if the username contains at least one letter, number, or punctuation mark.
# If so, prompt the user with an option to choose whether to hide or show their password input.

# Ask the user to enter "X" to hide their password or "S" to see their password while typing.
# Convert the input to lowercase and remove unnecessary spaces to avoid case sensitivity issues.

# If the user chooses "X", use getpass to hide the password input.
# If the user chooses "S", use a normal input function to display the password while typing.
# If the input is invalid, display an error message.

# Check if the password is too short (less than 6 characters).
# If so, inform the user that the password must be at least 6 characters long.

# Check if the password is weak:
# - It must be longer than 6 characters.
# - It should contain only letters (no numbers or punctuation).

# Check if the password is medium strength:
# - It must be longer than 6 characters.
# - It should contain both letters and numbers, but no punctuation.

# Check if the password is strong:
# - It must be longer than 6 characters.
# - It should contain letters, numbers, and at least one punctuation character.

# Call the function to execute the password checker.

"""
Aaron Molina
PasswordChecker prompts the user to enter a password and checks if that password is valid or not
"""

# created a method for this file to return the user's input.
def Correct_Password_Response():
    value = True

# created a variable named password
password = str

# created a variable called specialCharacter to make a list of the specific special characters the password must have.
specialCharacter = ['!', '@', '#', '$', '%']

# created a variable to tell the statement is true


    # created an if statement to check if the provided input has less than 8 characters
def ValidLength(password):
    if len(password) < 8:
        value = False# created a variable to tell statement is false
    else:
        value = True

    return value

    # created an if statement to check if the provided input has no digits
def HasNumber(password):
    if password.isdigit():
        value = False# created a variable to tell statement is false
    else:
        value = True

    return value

    # created an if statement to check if the provided input has no special characters form the list provided above
def HasSymbol(password):
    if not any(char in specialCharacter for char in password):
        value = False# created a variable to tell statement is false
    else:
        value = True

    return value
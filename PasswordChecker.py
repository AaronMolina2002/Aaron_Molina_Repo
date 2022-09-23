"""
Aaron Molina
PasswordChecker prompts the user to enter a password and checks if that password is valid or not
"""

# created a method for this file to return the user's input.
def Correct_Password_Response(password):

    # created a variable named password to ask the user to provide a password.
    password = input("Please enter a password: ")

    # created a variable called specialCharacter to make a list of the specific special characters the password must have.
    specialCharacter = ['!', '@', '#', '$', '%']

    # created a variable to tell the statement is true
    value = True

    # created an if statement to check if the provided input has less than 8 characters
    if len(password) < 8:
        print("Make sure your password has at least 8 characters.")# prints out message to tell user their password needs at least 8 characters
        value = False# created a variable to tell statement is false

    # created an if statement to check if the provided input has no digits
    if password.isdigit():
        print("Make sure your password has at least one number in it.")# prints out message telling user their password needs at least one digit
        value = False# created a variable to tell statement is false

    # created an if statement to check if the provided input has no special characters form the list provided above
    if not any(char in specialCharacter for char in password):
        print("Make sure your password has at least one special character.")# prints out message telling user they need at least one special character
        value = False# created a variable to tell statement is false

        # returns the variable value
        return value
    #created an else statement to check if the above input meets all the requirements
    else:
        print("Your password is valid.")# prints out message to user telling them their password is valid
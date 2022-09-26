"""
Aaron Molina
Imports the FancyCalculator, SimpleCalculator, and PasswordChecker to use each of those files in one file
"""

# import all the python files we want for this file.
import FancyCalculator


# create a main method
def main():

    # create a variable to ask the user for a program they wish to run.
    program = input("Enter a program you wish to run, Simple Calculator, Fancy Calculator, or Password checker? ")

    # create if statements for the password checker file
    if program == "Password checker":
        password = input("Please enter a password: ")# created variable to prompts user to enter a password and stores that input in the variable
        PasswordChecker.Correct_Password_Response(password)# goes to the PasswordChecker file
        print("Your password is {0}".format(password))# prints to user their password they inputed

    # created if statement for the simple calculator file
    elif program == "Simple Calculator":
        SimpleCalculator.Simple_Calculator()# goes to the SimpleCalculator file

    # created if statement for the fancy calculator file
    elif program == "Fancy Calculator":
        result = FancyCalculator.Fancy_Calculator()# created variable that goes to the FancyCalculator file
        print("The total is {0}".format(result))# prints out the users total and formats the above variable

# create an if statement to end the code.
if __name__ == "__main__":
    main()
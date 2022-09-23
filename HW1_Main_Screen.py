# import all the python files we want for this file.
import SimpleCalculator
import FancyCalculator
import PasswordChecker
import re
# create a main method
def main():

# create a variable to ask the user for a program they wish to run.
    program = input("Enter a program you wish to run, Simple Calculator, Fancy Calculator, or Password checker? ")

# create if statements for each program the user chooses to run.
    if program == "Password checker":
        password = input("Please enter a password: ")
        result = PasswordChecker.Correct_Password_Response(password)
        print("Your password is {0}".format(password))

    elif program == "Simple Calculator":
        SimpleCalculator.Simple_Calculator()

    elif program == "Fancy Calculator":
        result = FancyCalculator.Fancy_Calculator()
        print("The total is {0}".format(result))

# create an if statement to end the code.
if __name__ == "__main__":
    main()
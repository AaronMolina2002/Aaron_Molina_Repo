"""
Aaron Molina
SimpleCalculator takes one input from a user, then asks for an operation sign, then asks for another number and
calcultes the equation the user gave it and prints out the result.
"""

# created a main method
def Simple_Calculator():

    # asks the user for a number, converts that input to a float, and stores that value in a variable
    num1 = float(input("Please enter a value for the first number: "))

    # asks the user for an operator sign and stores that value in a variable
    operator = input("Please enter an operator you wish to use: ")

    # asks the user for a number, converts that input to a float, and stores the value in a variable
    num2 = float(input("Please enter a value for the second number: "))

    # if statement for the operator sign "+"
    if operator == "+":
        total = str(num1 + num2)# calculates the equation for addition and stores that value in a variable
        print("The total is: " + total)# prints out to the user their answer

    # if statement for the operator sign "-"
    if operator == "-":
        total = str(num1 - num2)# calculates the equation for subtraction and stores that value in a variable
        print("The total is: " + total)# prints out to the user their answer

    # if statement for the operator sign "*"
    if operator == "*":
        total = str(num1 * num2)# calculates the equation for multiplication and stores that value in a variable
        print("The total is: " + total)# prints out to the user their answer

    # if statement fo the operator sign "/"
    if operator == "/":
        total = str(num1 / num2)# calculates the equation for division and stores that value in a variable
        print("The total is: " + total)# prints out to the user their answer
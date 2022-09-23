"""
This is a fancy-ish calculator.
This accepts one user input, the equation
prints out the output
"""
def Fancy_Calculator():

    # Display a message to user.
    print("Hello user, this is a fancy calculator.")
    equation = (input("Provide me with an equation"))

    # extract the first value of the equation and convert it into an integer. Display the value of the first number.
    val1 = int(equation.split(' ')[0])
    print(val1)

    # extract the operation sign from the equation. Display the operation.
    op = equation.split(' ')[1]
    print(op)

    # extract the second value of the equation and convert it into an integer. Display the value of the second number.
    val2 = int(equation.split(' ')[2])
    print(val2)

    # create an if statement for the addition operation to allow the full equation to do addition.
    if op == "+":
        total = str(val1 + val2)# add a variable named total to add both values.

    # create an if statement for the subtraction operation to allow the full equation to do subtraction.
    if op == "-":
        total = str(val1 - val2)# add a variable named total to subtract both values.

    # create an if statement for the division operation to allow the full equation to do division.
    if op == "/":
        total = str(val1 / val2)# add a variable named total to divide both values.

    # create an if statement for the multiplication operation to allow the full equation to do multiplication.
    if op == "*":
        total = str(val1 * val2)# add a variable named total to multiple both values.

    return total
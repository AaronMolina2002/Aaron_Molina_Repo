num1 = int(input("Please enter a value for the first number: "))

operator = input("Please enter an operator you wish to use: ")

num2 = int(input("Please enter a value for the second number: "))

if operator == "+":
    total = str(num1 + num2)
    print("The total is: " + total)

if operator == "-":
    total = str(num1 - num2)
    print("The total is: " + total)

if operator == "*":
     total = str(num1 * num2)
     print("The total is: " + total)

if operator == "/":
    total = str(num1 / num2)
    print("The total is: " + total)
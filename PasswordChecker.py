def Correct_Password_Response(password):

    password = input("Please enter a password: ")

    specialCharacter = ['!', '@', '#', '$', '%']

    value = True

    if len(password) < 8:
        print("Make sure your password has at least 8 characters.")
        value = False

    if password.isdigit():
        print("Make sure your password has at least one number in it.")
        value = False

    if not any(char in specialCharacter for char in password):
        print("Make sure your password has at least one special character.")
        value = False

        return value

    else:
        print("Your password is ready.")

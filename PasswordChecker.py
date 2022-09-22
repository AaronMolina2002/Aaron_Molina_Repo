def Correct_Password_Response(password):
    return password

    password = input("Enter a password: ")

    specialCharacter = ['!', '@', '#', '$', '%']

    if len(password) < 8:
        print("Make sure your password has at least 8 characters.")

    if password.isdigit():
        print("Make sure your password has at least one number in it.")

    if not any(char in specialCharacter for char in password):
        print("Make sure your password has at least one special character.")

    else:
        print("Your password is ready.")

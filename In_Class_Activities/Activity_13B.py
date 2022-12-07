from In_Class_Practices import DBConnector


def CheckLogin(username, password):
    """

    :param username:
    :param password:
    :return:
    """
    # Check whether user and pass exist

    my_db = DBConnector.MyDB()
    sql_statement = "SELECT count(*) FROM AaronMolina_Users WHERE (AaronMolina_Users.Username = %s AND AaronMolina_Users.Password = %s);"

    result = my_db.query(sql_statement, (username, password))[0][0]
    if result != 0:
        # Return True
        return True
    return False


def CheckAdmin(nameOfUser):
    """
       First style of a method which verifies whether a provided user is an Admin
       :param nameOfUser: string of the user name
       :param passOfUser: string of the password
       :return: True if the user and password exist, otherwise False.
    """
    my_db = DBConnector.MyDB()
    sql_statement = "SELECT admin FROM AaronMolina_Users WHERE (AaronMolina_Users.Username = %s);"

    try:
        bool(my_db.query(sql_statement, [nameOfUser])[0][0])
    except:
        return False
    return True


def main():
    """
    Main screen for the web scrapping file
    :return:
    """
    user = input("Provide me with user name")
    password = input("Provide me with password")
    if(CheckLogin(user, password)):
        print("Welcome")
    else:
        print("No access")

    User = "User3"
    print("User is Admin : ", CheckAdmin(User))

if __name__ == "__main__":
    main()
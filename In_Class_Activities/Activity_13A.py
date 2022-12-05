"""
SQL Injection Example

"""
from In_Class_Practices import DBConnector as DBC

# Connect to DB
my_db = DBC.MyDB()


def CreateTablesAndFillData():
    """
    This creates one table (users) and inserts three rows, each represents a username and a password.
    """

    # Your code goes here.
    userName1 = "User1"
    password1 = "pass1"
    admin1 = "true"
    userName2 = "User2"
    password2 = "pass2"
    admin2 = "false"
    userName3 = "User3"
    password3 = "pass3"
    admin3 = "false"

    sqlCommand = 'CREATE TABLE IF NOT EXISTS AaronMolina_Users (Username  VARCHAR, Password  VARCHAR, Admin BOOL);'
    my_db.query(sqlCommand, '')

    sqlCommand = 'INSERT INTO AaronMolina_Users VALUES(%s, %s, %s);'
    my_db.query(sqlCommand, (userName1, password1, admin1,))
    my_db.query(sqlCommand, (userName2, password2, admin2,))
    my_db.query(sqlCommand, (userName3, password3, admin3,))

def main():
    """
    Main screen for the web scrapping file
    :return:
    """
    # Create the table and add data
    CreateTablesAndFillData()


if __name__ == "__main__":
    main()

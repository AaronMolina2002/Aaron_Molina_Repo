"""
This class tests the connection to your DB by creating a test table
"""

# Import the connector class
import DBTruncator

# Create a new instance of the DB
my_db = DBTruncator.MyDB()

# SQL command to create a new table
sqlCommand = 'CREATE TABLE IF NOT EXISTS Molina_Aaron_Table (MID  VARCHAR, MName  VARCHAR);'

# Message to display upon table creation. Not integrated yet.
sqlMessage = 'Table Test created successfully. Please access pgAdmin to verify table was created successfully'

# Execute the SQL command.
my_db.query(sqlCommand, '')
#!/usr/bin/python3
"""
Lists all states with a name starting with N from the database 'hbtn_0e_0_usa'
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get the arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    # Execute the query
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    # Fetch all results into 'rows'
    rows = cursor.fetchall()

    # Print each tuple (id, name)
    for row in rows:
        print(row)

    # Close the cursor and the connection
    cursor.close()
    db.close()

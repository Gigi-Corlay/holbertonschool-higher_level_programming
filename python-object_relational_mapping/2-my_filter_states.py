#!/usr/bin/python3
"""
Displays the first state in the states table where name matches the argument
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    # Use parameterized query and fetch only one row
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC LIMIT 1"
    cursor.execute(query, (state_name,))

    row = cursor.fetchone()  # Fetch only the first matching row
    if row:
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()

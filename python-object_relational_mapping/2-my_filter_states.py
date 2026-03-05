#!/usr/bin/python3
"""
Displays all values in the states table where name matches the argument
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

    # Execute the query using format to insert the state name
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cursor.execute(query)

    # Fetch all results
    rows = cursor.fetchall()

    # Print each tuple (id, name)
    for row in rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()
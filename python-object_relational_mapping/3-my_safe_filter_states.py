#!/usr/bin/python3
"""
Displays all records in the states table
where the name matches the given argument
(Safe from SQL injection)
"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py <user> <password> <database> <state_name>")
        sys.exit(1)

    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    # Safe query using parameterized statement
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))  # the parameter is passed as a tuple

    # Fetch all results
    rows = cursor.fetchall()

    # Print each tuple (id, name)
    for row in rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()

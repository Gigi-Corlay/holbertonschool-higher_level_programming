#!/usr/bin/python3
"""
This script lists all cities of a given state from the database hbtn_0e_4_usa.
It takes 4 arguments: mysql username, mysql password, database name, and state name.
Results are displayed as a comma-separated list, sorted by cities.id.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check for the correct number of arguments
    if len(sys.argv) != 5:
        print("Usage: ./5-filter_cities.py <user> <password> <database> <state_name>")
        sys.exit(1)

    # Assign arguments to variables
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=database
    )
    cursor = db.cursor()

    # Prepare the SQL query to select cities from the given state
    # Use parameterized query to prevent SQL injection
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    # Fetch all results
    rows = cursor.fetchall()

    # Print cities as a comma-separated list
    print(", ".join([row[0] for row in rows]))

    # Close cursor and database connection
    cursor.close()
    db.close()
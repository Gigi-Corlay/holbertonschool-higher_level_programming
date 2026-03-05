#!/usr/bin/python3

import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

import sys

"""
Lists all states from the database hbtn_0e_0_usa
"""
if __name__ == "__main__":
    # Get MySQL credentials and database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server on localhost:3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and display all rows
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
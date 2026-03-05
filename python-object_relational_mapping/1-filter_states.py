#!/usr/bin/python3
"""
Lists all states with a name starting with N from the database 'hbtn_0e_0_usa'
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Récupère les arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connexion à MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    # Exécute la requête
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    # Récupère tous les résultats dans 'rows'
    rows = cursor.fetchall()

    # Affiche chaque tuple (id, name)
    for row in rows:
        print(row)

    # Ferme le curseur et la connexion
    cursor.close()
    db.close()
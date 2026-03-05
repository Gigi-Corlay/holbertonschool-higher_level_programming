#!/usr/bin/python3
"""
Affiche tous les enregistrements de la table states
dont le nom correspond à l'argument fourni
(Sécurisé contre les injections SQL)
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

    # Connexion à MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    # Requête sécurisée avec paramètre
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))  # le paramètre est passé dans un tuple

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
    
#!/usr/bin/python3
import MySQLdb
# Import du module MySQLdb pour interagir avec MySQL

# Ce bloc ne s'exécute que si le script est lancé directement
if __name__ == "__main__":
    """
    Connexion à la base de données MySQL
    - host : serveur MySQL (ici localhost)
    - port : port MySQL (3306 par défaut)
    - user : nom d'utilisateur MySQL
    - passwd : mot de passe MySQL
    - db : nom de la base de données
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="password",
        db="my_database"
    )

    # Création d'un curseur pour exécuter des requêtes SQL
    cursor = db.cursor()

    """
    Exécution d'une requête SQL pour récupérer toutes les lignes de la table 'states'
    Les résultats sont triés par 'id' en ordre croissant
    """
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Récupération de toutes les lignes retournées par la requête
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Fermeture du curseur pour libérer les ressources
    cursor.close()
    
    # Fermeture de la connexion à la base de données
    db.close()

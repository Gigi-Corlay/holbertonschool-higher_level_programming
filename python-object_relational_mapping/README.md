# Connexion à une base de données MySQL avec Python

## 1️⃣ Comment se connecter à une base de données MySQL depuis un script Python

Pour connecter Python à MySQL, on utilise une bibliothèque comme :

- `mysql-connector-python` (officielle de Oracle)
- `PyMySQL`
- `MySQLdb`

La plus simple pour commencer est **mysql-connector-python**.

### Installation

```bash
pip install mysql-connector-python
```
### Exemple de connexion
```python
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="my_database"
)

cursor = db.cursor()

print("Connexion réussie")
```
### Explication
- host → adresse du serveur MySQL
- user → nom d'utilisateur MySQL
- password → mot de passe
- database → base de données utilisée
- cursor sert à exécuter les requêtes SQL.

## 2️⃣ Comment faire un SELECT dans une table MySQL depuis Python

Un **SELECT** permet de lire les données d'une table.

### Exemple
```python
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="my_database"
)

cursor = db.cursor()

cursor.execute("SELECT * FROM users")

results = cursor.fetchall()

for row in results:
    print(row)
```

### Explication
- cursor.execute() → exécute la requête SQL
- fetchall() → récupère toutes les lignes
- chaque row représente une ligne de la table

### Exemple de résultat :
```
(1, 'Alice', 25)
(2, 'Bob', 30)
```

## 3️⃣ Comment faire un INSERT dans une table MySQL depuis Python
Un **INSERT** sert à **ajouter une ligne dans une table**.

### Exemple
```python
sql = "INSERT INTO users (name, age) VALUES (%s, %s)"
values = ("Alice", 25)

cursor.execute(sql, values)

db.commit()
```

### Explication importante
- ```%s``` = **placeholder** pour éviter les **SQL injections**
- ```execute()``` remplace automatiquement les valeurs
- ```commit()``` valide les modifications dans la base
Sans commit(), la modification **ne sera pas enregistrée**.

## 4️⃣ Que signifie ORM
**ORM = Object Relational Mapping**

Un ORM permet de **manipuler la base de données avec des objets Python au lieu d’écrire du SQL**.

Bibliothèques ORM populaires :
-SQLAlchemy
-Django ORM
- Peewee

### Sans ORM

**SQL :**
```SQL
SELECT * FROM users;
```
**Python :**
```python
cursor.execute("SELECT * FROM users")
```

### Avec ORM
**Python :**
```python
users = session.query(User).all()
```
On **ne manipule plus SQL directement.**

## 5️⃣ Comment mapper une classe Python à une table MySQL

Avec un ORM comme **SQLAlchemy**, on peut **associer une classe Python à une table SQL.**

### Exemple avec SQLAlchemy
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
```
### Correspondance
| Classe Python | Table MySQL |
|---------------|-------------|
| User | users |
| id | colonne id |
| name | colonne name |
| age | colonne age |

### Insérer avec ORM
```python
new_user = User(name="Alice", age=25)

session.add(new_user)
session.commit()
```


## 📌 Résumé

| Concept | Explication |
|--------|-------------|
| Connexion MySQL | bibliothèque Python pour se connecter à MySQL |
| SELECT | récupérer des données |
| INSERT | ajouter des données |
| ORM | manipuler la base avec des objets |
| Mapping | associer classe Python ↔ table SQL |
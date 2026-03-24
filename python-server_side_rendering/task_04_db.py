#!/usr/bin/python3

from flask import Flask, request, render_template, jsonify
import csv
import io
import sqlite3

app = Flask(__name__)


def fetch_products_from_db():
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row  # permet de récupérer des dicts
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()
        products = [dict(row) for row in rows]
        conn.close()
        return products
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None  # ou [] selon ce que vous préférez


# Exemple de données JSON statiques (pour source=json)
json_products = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 799.99},
    {"id": 2, "name": "Coffee Mug", "category": "Home Goods", "price": 15.99}
]


# Fonction pour lire CSV depuis un fichier ou chaîne
def fetch_products_from_csv():
    csv_data = """id,name,category,price
1,Laptop,Electronics,799.99
2,Coffee Mug,Home Goods,15.99
"""
    f = io.StringIO(csv_data)
    reader = csv.DictReader(f)

    return list(reader)


@app.route('/products')
def products():
    source = request.args.get('source', 'json').lower()

    if source == 'json':
        data = json_products
    elif source == 'csv':
        data = fetch_products_from_csv()
    elif source == 'sql':
        data = fetch_products_from_db()
        if data is None:
            return "Database error", 500
    else:
        return "Wrong source", 400

    # Rendu du template avec les données
    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True)

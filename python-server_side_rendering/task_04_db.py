#!/usr/bin/python3

import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

"""
Données JSON statiques pour testing
"""
json_products = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 799.99},
    {"id": 2, "name": "Coffee Mug", "category": "Home Goods", "price": 15.99}
]


# Fonctions de lecture des données
def fetch_products_from_csv(filename='products.csv'):
    """
    Lit les produits depuis un fichier CSV et retourne une liste de dicts
    """
    products = []
    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    row['id'] = int(row['id'])
                    row['price'] = float(row['price'])
                    products.append(row)
                except ValueError:
                    print(f"Erreur conversion CSV: {row}")
    except FileNotFoundError:
        print(f"Fichier CSV {filename} introuvable")
    return products


def fetch_products_from_db():
    """
    Lit les produits depuis SQLite et retourne une liste de dicts
    """
    products = []
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        products = [dict(row) for row in rows]
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
    return products


# Routes
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    """
    Affiche les items depuis items.json
    """
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            items_list = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []
    return render_template('items.html', items=items_list)


@app.route('/products')
def products():
    """
    Affiche les produits depuis JSON, CSV ou SQL, avec filtrage par id optionnel
    """
    source = request.args.get('source', 'json').lower()
    product_id = request.args.get('id')

    # Lecture des données selon la source
    if source == 'json':
        data = json_products
    elif source == 'csv':
        data = fetch_products_from_csv()
    elif source == 'sql':
        data = fetch_products_from_db()
    else:
        return render_template('product_display.html',
                               error="Wrong source", products=[])

    # Filtrage par ID si fourni
    if product_id:
        try:
            product_id = int(product_id)
            filtered = [p for p in data if p['id'] == product_id]
            if not filtered:
                return render_template('product_display.html',
                                       error="Product not found", products=[])
            data = filtered
        except ValueError:
            return render_template('product_display.html',
                                   error="Invalid ID format", products=[])

    return render_template('product_display.html', products=data)


# Exécution de l'application
if __name__ == '__main__':
    app.run(debug=True, port=5000)

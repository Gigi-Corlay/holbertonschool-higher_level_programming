#!/usr/bin/python3
import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


# Reading functions
def read_json(filename='products.json'):
    """
    Lire les données depuis un fichier JSON
    """
    with open(filename, 'r') as f:
        return json.load(f)


def read_csv(filename='products.csv'):
    """
    Lire les données depuis un fichier CSV et convertir en dict
    """
    products = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products


def read_sql():  # sourcery skip: extract-method, for-append-to-extend
    """
    Lire les données depuis SQLite (products.db)
    """
    products = []
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        for row in rows:
            products.append(dict(row))
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
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
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            items_list = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []
    return render_template('items.html', items=items_list)


@app.route('/products')
def products():
    source = request.args.get('source', default='json').lower()
    product_id = request.args.get('id', type=int)

    # Validation du paramètre source
    if source not in ['json', 'csv', 'sql']:
        return render_template(
            'product_display.html', 
            error="Wrong source", 
            products=[]
        )

    # Lecture des données selon la source
    try:
        if source == 'json':
            data = read_json('products.json')
        elif source == 'csv':
            data = read_csv('products.csv')
        elif source == 'sql':
            data = read_sql()
    except FileNotFoundError:
        return render_template(
            'product_display.html',
            error="File not found",
            products=[]
        )
    except Exception as e:
        return render_template(
            'product_display.html',
            error=f"Data error: {str(e)}",
            products=[]
        )

    """
    Filtrage par ID si fourni
    """
    if product_id:
        data = [p for p in data if p.get('id') == product_id]
        if not data:
            return render_template(
                'product_display.html',
                error="Product not found",
                products=[]
            )

    # Affichage des produits
    return render_template('product_display.html', products=data, error=None)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

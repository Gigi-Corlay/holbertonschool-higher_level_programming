#!/usr/bin/python3

import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

# --- Static JSON fallback data ---
json_products = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 799.99},
    {"id": 2, "name": "Coffee Mug", "category": "Home Goods", "price": 15.99}
]


# --- Data reading functions ---
def read_json(filename='products.json'):
    """
    Reads products from a JSON file and returns a list of dictionaries.
    """
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def read_csv(filename='products.csv'):
    """
    Reads products from a CSV file and returns a list of dictionaries.
    """
    products = []
    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    products.append({
                        'id': int(row['id']),
                        'name': row['name'],
                        'category': row['category'],
                        'price': float(row['price'])
                    })
                except (ValueError, KeyError):
                    continue
    except FileNotFoundError:
        return []
    return products


def read_sql():
    """
    Reads products from SQLite database and returns a list of dictionaries.
    """
    try:
        with sqlite3.connect('products.db') as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, category, price FROM Products")
            rows = cursor.fetchall()
            return [dict(row) for row in rows]
    except sqlite3.Error:
        return []


# --- Routes ---
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
    Displays items from items.json
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
    Displays products from JSON, CSV, or SQL with optional ID filtering.
    """
    source = request.args.get('source', 'json').lower()
    product_id = request.args.get('id', type=int)

    # --- Select data source ---
    if source == 'json':
        data = read_json('products.json') or json_products
    elif source == 'csv':
        data = read_csv('products.csv') or json_products
    elif source == 'sql':
        data = read_sql() or json_products
    else:
        return render_template(
            'product_display.html',
            error="Wrong source",
            products=[]
            )

    # --- Optional filtering by ID ---
    if product_id is not None:
        filtered = [p for p in data if p.get('id') == product_id]
        if not filtered:
            return render_template(
                'product_display.html', 
                error=f"No product with ID {product_id}",
                products=[]
            )
        data = filtered

    return render_template('product_display.html', products=data, error=None)


# --- Run the application ---
if __name__ == '__main__':
    app.run(debug=True, port=5000)

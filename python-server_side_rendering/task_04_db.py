#!/usr/bin/python3

import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

# Fallback JSON data
json_products = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 799.99},
    {"id": 2, "name": "Coffee Mug", "category": "Home Goods", "price": 15.99}
]


# --- Data reading functions ---
def read_json(filename='products.json'):
    try:
        with open(filename, 'r') as f:
            return json.load(f), None
    except (FileNotFoundError, json.JSONDecodeError) as e:
        return None, f"JSON error: {str(e)}"


def read_csv(filename='products.csv'):
    try:
        products = []
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
        return products, None
    except FileNotFoundError:
        return None, f"CSV file '{filename}' not found"


def read_sql():
    try:
        with sqlite3.connect('products.db') as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, category, price FROM Products")
            rows = cursor.fetchall()
            return [dict(row) for row in rows], None
    except sqlite3.Error as e:
        return None, f"Database error: {str(e)}"


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
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            items_list = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []
    return render_template('items.html', items=items_list)


@app.route('/products')
def products():
    source = request.args.get('source', 'json').lower()
    product_id_str = request.args.get('id')

    # --- Select data source ---
    if source == 'json':
        data, error = read_json('products.json')
    elif source == 'csv':
        data, error = read_csv('products.csv')
    elif source == 'sql':
        data, error = read_sql()
    else:
        return render_template(
            'product_display.html',
            error="Wrong source",
            products=[]
        )

    # Use fallback if reading failed
    if error:
        data = json_products

    # --- Optional filtering by ID ---
    if product_id_str:
        try:
            product_id = int(product_id_str)
        except ValueError:
            return render_template(
                'product_display.html',
                error="ID must be an integer",
                products=[]
            )

        filtered = [p for p in data if p.get('id') == product_id]
        if not filtered:
            return render_template(
                'product_display.html',
                error=f"No product with ID {product_id}",
                products=[]
            )
        data = filtered

    return render_template('product_display.html', products=data, error=None)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

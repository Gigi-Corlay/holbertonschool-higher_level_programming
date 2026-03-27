#!/usr/bin/python3

import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

"""
Static JSON data for testing purposes
"""
json_products = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 799.99},
    {"id": 2, "name": "Coffee Mug", "category": "Home Goods", "price": 15.99}
]


# -----------------------------
# Database initialization
# -----------------------------
def create_database():
    """
    Creates the products.db SQLite database and populates it if empty.
    Called once at application startup.
    """
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')

    # Only insert if table is empty
    cursor.execute("SELECT COUNT(*) FROM Products")
    if cursor.fetchone()[0] == 0:
        cursor.execute('''
            INSERT INTO Products (id, name, category, price)
            VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99)
        ''')

    conn.commit()
    conn.close()


# -----------------------------
# CSV Reader
# -----------------------------
def fetch_products_from_csv(filename='products.csv'):
    """
    Reads products from a CSV file and returns a list of dictionaries.
    Returns (products, error_message).
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
                except (ValueError, KeyError) as e:
                    print(f"CSV conversion error on row {row}: {e}")

    except FileNotFoundError:
        return [], f"CSV file '{filename}' not found"
    except Exception as e:
        return [], f"CSV read error: {e}"

    return products, None


# -----------------------------
# Database Reader
# -----------------------------
def fetch_products_from_db():  # sourcery skip: extract-method
    """
    Reads products from the SQLite database.
    Returns (products, error_message).
    """
    conn = None
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()

        products = [dict(row) for row in rows]
        return products, None

    except sqlite3.Error as e:
        return [], f"Database error: {e}"

    finally:
        if conn:
            conn.close()


# -----------------------------
# Routes
# -----------------------------
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
    Displays products from JSON, CSV, or SQL, with optional filtering by ID.
    Usage:
        /products?source=json
        /products?source=csv
        /products?source=sql
        /products?source=json&id=1
    """
    source = request.args.get('source', type=str)
    product_id = request.args.get('id', type=int)

    data = []
    error = None

    # Select data source
    if source == 'json':
        data = json_products

    elif source == 'csv':
        data, error = fetch_products_from_csv()

    elif source == 'sql':
        data, error = fetch_products_from_db()

    else:
        error = "Wrong source"

    if error:
        return render_template('product_display.html', error=error, products=[])

    # Filter by ID
    if product_id is not None:
        filtered = [p for p in data if p['id'] == product_id]
        if not filtered:
            return render_template(
                'product_display.html',
                error=f"Product with id={product_id} not found",
                products=[]
            )
        data = filtered

    return render_template('product_display.html', products=data)


# -----------------------------
# Application entry point
# -----------------------------
if __name__ == '__main__':
    create_database()
    app.run(debug=True, port=5000)

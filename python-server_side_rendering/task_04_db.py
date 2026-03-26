#!/usr/bin/python3

from flask import Flask, request, render_template
import csv
import io
import sqlite3

app = Flask(__name__)

# Données JSON statiques
json_products = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 799.99},
    {"id": 2, "name": "Coffee Mug", "category": "Home Goods", "price": 15.99}
]


def fetch_products_from_csv():
    csv_data = """id,name,category,price
1,Laptop,Electronics,799.99
2,Coffee Mug,Home Goods,15.99
"""
    f = io.StringIO(csv_data)
    reader = csv.DictReader(f)
    products = []
    for row in reader:
        try:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
        except ValueError:
            print(f"Erreur conversion CSV: {row}")
    return products


def fetch_products_from_db():
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()
        products = [dict(row) for row in rows]
        conn.close()
        return products
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None


@app.route('/products')
def products():
    source = request.args.get('source', 'json').lower()
    product_id = request.args.get('id')

    # Sélection de la source
    if source == 'json':
        data = json_products
    elif source == 'csv':
        data = fetch_products_from_csv()
    elif source == 'sql':
        data = fetch_products_from_db()
        if data is None:
            return render_template('product_display.html', 
                                   error="Database error", products=[])
    else:
        return render_template('product_display.html', 
                               error="Wrong source", products=[])

    # Filtrer par ID si fourni
    if product_id:
        try:
            product_id = int(product_id)
            if filtered := [p for p in data if p['id'] == product_id]:
                data = filtered
            else:
                return render_template('product_display.html', 
                                       error="Product not found", products=[])
        except ValueError:
            return render_template('product_display.html', 
                                   error="Invalid ID format", products=[])

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

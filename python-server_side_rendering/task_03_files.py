#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


# Fonction pour lire JSON
def read_json(file_path='products.json'):
    try:
        with open(file_path) as f:
            return json.load(f)
    except Exception as e:
        print(f"Erreur lecture JSON: {e}")
        return []


# Fonction pour lire CSV
def read_csv(file_path='products.csv'):
    products = []
    try:
        with open(file_path) as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convertir id en int et price en float
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except Exception as e:
        print(f"Erreur lecture CSV: {e}")
    return products


# Route principale
@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    else:
        return render_template('product_display.html', error="Wrong source")

    # Filtrage par id si fourni
    if product_id:
        try:
            product_id = int(product_id)
            data = [p for p in data if p['id'] == product_id]
            if not data:
                return render_template('product_display.html', error="Product not found")
        except ValueError:
            return render_template('product_display.html', error="Invalid ID format")

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True)

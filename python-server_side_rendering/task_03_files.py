#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json(filename='products.json'):
    """Lit un fichier JSON et retourne une liste de produits"""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Erreur lecture JSON: {e}")
        return []


def read_csv(filename='products.csv'):
    """Lit un fichier CSV et retourne une liste de produits"""
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
    except Exception as e:
        print(f"Erreur lecture CSV: {e}")
    return products


@app.route('/products')
def products():
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id')

    # Vérifier la source
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source", products=[])

    # Lire les données
    data = read_json() if source == 'json' else read_csv()

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

#!/usr/bin/python3
"""
Rendering CSV, SQL and JSON data
"""

from flask import Flask, render_template, request
import sqlite3
import json
import csv

app = Flask(__file__)


def read_json():
    """
    Read data from products.json
    """
    with open('products.json', 'r') as file:
        return json.load(file)


def read_csv():
    """
    Read data and convert to json
    """
    products = []

    with open('products.csv', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)

    return products


def read_sql():
    """
    Read data and convert to json
    """
    try:
        conn = sqlite3.connect('products.db')

        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Products')

        products = cursor.fetchall()

        format_products = []
        for row in products:
            format_products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })

        return format_products
    except sqlite3.Error:
        return []


@app.route('/products')
def display_products():
    """
    Display all products or with id
    """
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    else:
        products = read_sql()

    if product_id:
        products = \
            [product for product in products if product['id'] == product_id]

        if not products:
            return render_template(
                'product_display.html',
                error="Product not found"
            )

    if not products:
        return render_template(
            'product_display.html',
            error="No products found"
        )
    return render_template(
        'product_display.html',
        products=products
    )


if __name__ == "__main__":
    app.run(debug=True)

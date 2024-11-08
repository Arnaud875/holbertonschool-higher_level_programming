#!/usr/bin/python3
"""
Rendering CSV and JSON data
"""


import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)


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


@app.route('/products')
def display_products():
    """
    Display all products or with id
    """
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    if source == 'json':
        products = read_json()
    else:
        products = read_csv()

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


if __name__ == '__main__':
    app.run(debug=True)

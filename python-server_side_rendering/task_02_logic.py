#!/usr/bin/python3
"""
Use template with flask
"""


from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/items')
def items():
    """
    Display items to html
    """
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
    except:
        data = {'items': []}

    return render_template('items.html', items=data['items'])


if __name__ == '__main__':
    app.run(debug=True)

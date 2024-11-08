#!/usr/bin/python3
"""
Use templates with Flask
"""


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """
    View index.html template
    """
    return render_template('index.html')


@app.route('/about')
def about():
    """
    View about.html template
    """
    return render_template('about.html')


@app.route('/contact')
def contact():
    """
    View contact.html template
    """
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)

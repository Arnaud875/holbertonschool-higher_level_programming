#!/usr/bin/python3
"""
Make simple api with Flask library
"""
from flask import Flask, jsonify, request


USERS_DATA = []
app = Flask(__name__)


def find_user(username):
    """
    Get user with username or None
    """
    for user in USERS_DATA:
        if user["username"] == username:
            return user
    return None


@app.route("/")
def home():
    """
    Default endpoint
    """
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    """
    Status endpoint to check if server is alive
    """
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """
    Get user endpoint to find user data with username
    """
    user = find_user(username)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Add user endpoint to add user data
    """

    if not request.json.get("username"):
        return jsonify({ "error": "Username is required" }), 400

    if not find_user(request.json["username"]):
        USERS_DATA.append(request.json)

    return jsonify({
        "message": "User added",
        "user": request.json
    }), 201


@app.route("/data")
def data():
    """
    Get data endpoint to get all users stocked in memory
    """
    all_username = []
    for user in USERS_DATA:
        all_username.append(user["username"])
    return jsonify(all_username)


if __name__ == "__main__":
    app.run()

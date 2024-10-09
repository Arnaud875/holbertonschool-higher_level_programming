#!/usr/bin/python3
"""
Make simple auth api with Flask, JWT and BasicAuth
"""
from flask import Flask, jsonify, request
from flask_jwt_extended import get_jwt_identity, \
    create_access_token, JWTManager, jwt_required
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "I_am_god"

jwt = JWTManager(app)
auth = HTTPBasicAuth()

users = {
    "user1": {
        "username": "user1",
        "password": "<hashed_password>",
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": "<hashed_password>",
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """
    Check if user exist in "database"
    """
    if username in users:
        if check_password_hash(users[username]["password"], password):
            return username
    return None


@app.route("/login", methods=["POST"])
def user_login():
    """
    Create a new user and return jwt access token
    """
    username = request.json["username"]
    password = request.json["password"]

    user = users.get(username)

    if not user:
        return jsonify({"error": "Invalid credentials"}), 401

    if not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity={"username": username, "role": user["role"]})
    return jsonify(access_token=access_token), 200


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """
    Check if user exist with BasicAuth
    """
    return jsonify({"Basic Auth": "Access Granted"}), 200


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """
    Check if is a valid jwt token
    """
    return jsonify({"JWT Auth": "Access Granted"}), 200


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """
    Check if user is a Admin
    """
    if get_jwt_identity()["role"] != "admin":
        return "403 Forbidden", 403
    return jsonify({"Admin Access": "Granted"}), 200


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Handle unauthorized error of JWT
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Handle invalid token error of JWT
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """
    Handle expired token error of JWT
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """
    Handle revoked token error of JWT
    """
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """
    Handle needs fresh token error of JWT
    """
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()

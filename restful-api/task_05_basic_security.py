#!/usr/bin/python3
"""
Module: task_05_basic_security
Description: Flask API with Basic Authentication and JWT Authentication.
Routes:
    /basic-protected  -> Protected by Basic Auth
    /login            -> Generates JWT token
    /jwt-protected    -> Protected by JWT
    /admin-only       -> Admin-only access protected by JWT
"""

from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)

"""
Configuration JWT
"""
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

"""
Gestionnaires d’erreurs JWT
"""
@jwt.unauthorized_loader
def handle_missing_token(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token(err):
    return jsonify({"error": "Token has expired"}), 401

# Optionnel : pour les tests stricts
@jwt.revoked_token_loader
def handle_revoked_token(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token(err):
    return jsonify({"error": "Fresh token required"}), 401

"""
Basic Auth
"""
auth = HTTPBasicAuth()

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    if username in users:
        user = users[username]
        if check_password_hash(user["password"], password):
            return user
    return None

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

"""
JWT Routes
"""
@app.route("/login", methods=["POST"])
def login():
    """
    Login route to generate JWT token.
    Expects JSON payload: {"username": "user", "password": "pass"}
    Returns JWT token if credentials are valid, else 401.
    """
    data = request.get_json()
    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Missing username or password"}), 401

    username = data.get("username")
    password = data.get("password")

    if username in users and check_password_hash(users[username]["password"], password):
        access_token = create_access_token(
            identity={"username": username, "role": users[username]["role"]}
        )
        return jsonify({"access_token": access_token}), 200

    return jsonify({"error": "Invalid credentials"}), 401

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

@app.route("/admin-only")
@jwt_required()
def admin_only():
    """
    Admin-only route.
    Checks JWT token and ensures user has role 'admin'.
    Returns 403 if user is not admin.
    """
    identity = get_jwt_identity()
    if identity["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()

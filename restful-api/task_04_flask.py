#!/usr/bin/python3
"""
task_04_flask.py
A simple RESTful API using Flask to manage users.
Handles GET and POST requests with JSON responses.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    """
    GET /
    Returns a welcome message for the API.
    """
    return "Welcome to the Flask API!"


users = {}


@app.route("/data")
def data():
    """
    GET /data
    Returns a JSON list of all usernames stored in the API.
    """
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route("/status")
def status():
    """
    GET /status
    Returns OK to indicate the API is running.
    """
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """
    GET /users/<username>
    Returns the full object corresponding to the provided username.
    If the user does not exist, returns 404 with an error message.
    """
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    POST /add_user
    Adds a new user to the API.
    Validates JSON body, checks for existing username, and required fields.
    Returns appropriate HTTP status codes:
      - 201: User added
      - 400: Invalid JSON or missing username
      - 409: Username already exists
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data
    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run(port=5001)

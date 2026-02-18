#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the Flask API!"

users = {}

users["jane"] = {
    "username": "jane",
    "name": "Jane",
    "age": 28,
    "city": "Los Angeles"
}


@app.route("/data")
def data():
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
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

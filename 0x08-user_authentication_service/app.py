#!/usr/bin/env python3
"""[Flask app]"""
from flask import Flask, jsonify, request
from auth import Auth
app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=["GET"], strict_slashes=False)
def greet() -> str:
    """[GET /]
    """
    return jsonify({"message": "bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """POST /users
    register a user
    Args:
        request ([type]): [description]
    """
    try:
        email = request.form["email"]
        password = request.form["password"]
        user = AUTH.register_user(email, password)
        if user:
            return jsonify({"email": email, "message": "user_created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

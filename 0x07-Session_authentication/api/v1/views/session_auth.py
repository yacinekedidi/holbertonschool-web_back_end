#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_login():
    """ POST /api/v1/auth_session/login
    """
    email = request.form.get("email")
    password = request.form.get("password")
    if not email or not len(email):
        return jsonify({"error": "email missing"}), 400
    if not password or not len(password):
        return jsonify({"error": "password missing"}), 400
    u_list = User().search({"email": email})
    if not len(u_list):
        return jsonify({"error": "no user found for this email"}), 404
    u = u_list[0]
    if not u.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    session_id = auth.create_session(u.id)
    response = jsonify(u.to_json())
    response.set_cookie(getenv("SESSION_NAME"), session_id)
    return response


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def session_logout():
    """ DELETE /api/v1/auth_session/logout
    """
    from api.v1.app import auth
    is_logged_out = auth.destroy_session(request)
    if not is_logged_out:
        return False, abort(404)
    return jsonify({}), 200

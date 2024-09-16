#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv

from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")
import os

from flask import Flask, abort, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.errorhandler(404)
def not_found(error) -> str:
    """Not found handler"""
    return jsonify({"error": "Not found"}, 200)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "8000")
    app.run(host=host, port=port)

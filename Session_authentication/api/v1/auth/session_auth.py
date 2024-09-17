#!/usr/bin/env python3
""" Module of Session Authentication
"""
from flask import request

from api.v1.auth.auth import Auth
from api.v1.views import app_views
from models.user import User


class SessionAuth(Auth):
    """
    Session Auth class
    """

    pass

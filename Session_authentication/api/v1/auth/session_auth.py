#!/usr/bin/env python3
""" Module of Session Authentication
"""
from flask import request

from api.v1.auth.auth import Auth
from api.v1.views import app_views
from models.user import User
import uuid


class SessionAuth(Auth):
    """
    Session Auth class
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create session"""
        if user_id is None or type(user_id) != str:
            return None
        session_id = str(uuid.uuid4())
        SessionAuth.user_id_by_session_id[session_id] = user_id
        return session_id

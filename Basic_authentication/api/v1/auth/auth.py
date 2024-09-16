#!/usr/bin/env python3


"""
Auth class
"""
from flask import request
from api.v1.views import app_views
from models.user import User
from typing import List, TypeVar


class Auth:
    """Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require Auth"""
        return False

    def authorization_header(self, request=None) -> str:
        """Authorization header"""
        return

    def current_user(self, request=None) -> TypeVar("User"):
        """Current user"""
        return

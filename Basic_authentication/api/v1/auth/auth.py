from flask import request
from api.v1.views import app_views
from models.user import User
from typing import List
from flask import jsonify
from models import storage


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

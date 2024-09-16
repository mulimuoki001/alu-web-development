#!/usr/bin/env python3
""" Module of Basic Auth
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic Auth class"""

    def extract_base64_authorization(self, authorization_header: str) -> str:
        """Extract base64"""
        if authorization_header is None:
            return None
        if type(authorization_header) != str:
            return None
        if authorization_header[:6] != "Basic ":
            return None
        return authorization_header[6:]

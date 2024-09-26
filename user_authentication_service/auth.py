#!/usr/bin/env python3


"""Hashed password management for the 'users' table."""
from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> str:
    """
    Hashes a password using bcrypt.

    Args:
        password (str): Password to hash.

    Returns:
        str: Hashed password.
    """

    return hashpw(password.encode("utf-8"), gensalt()).decode("utf-8")

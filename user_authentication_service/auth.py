#!/usr/bin/env python3


"""Hashed password management for the 'users' table."""
from bcrypt import hashpw, gensalt
from sqlalchemy.orm.exc import NoResultFound

from db import DB


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> None:
        """
        Registers a new user in the database.

        Args:
            email (str): User's email address.
            password (str): Password for the user.
        """

        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            self._db.add_user(email, _hash_password(password))


def _hash_password(password: str) -> str:
    """
    Hashes a password using bcrypt.

    Args:
        password (str): Password to hash.

    Returns:
        str: Hashed password.
    """

    return hashpw(password.encode("utf-8"), gensalt()).decode("utf-8")

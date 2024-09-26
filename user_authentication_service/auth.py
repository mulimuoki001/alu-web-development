#!/usr/bin/env python3


"""Hashed password management for the 'users' table."""
from bcrypt import hashpw, gensalt, checkpw
from sqlalchemy.orm.exc import NoResultFound
from user import User
import uuid

from db import DB


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
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

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validates a user's login credentials.

        Args:
            email (str): User's email address.
            password (str): Password for the user.

        Returns:
            bool: True if the login is valid, False otherwise.
        """

        try:
            user = self._db.find_user_by(email=email)
            return checkpw(
                password.encode("utf-8"), user.hashed_password.encode("utf-8")
            )
        except NoResultFound:
            return False

    def _generate_uuid() -> str:
        """
        Generates a random UUID.

        Returns:
            str: Random UUID.
        """

        return str(uuid.uuid4())


def _hash_password(password: str) -> str:
    """
    Hashes a password using bcrypt.

    Args:
        password (str): Password to hash.

    Returns:
        str: Hashed password.
    """

    return hashpw(password.encode("utf-8"), gensalt()).decode("utf-8")

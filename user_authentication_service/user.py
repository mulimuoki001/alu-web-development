#!/usr/bin/env python3


"""SQLAlchemy model for the 'users' table."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    SQLAlchemy model for the 'users' table.

    Attributes:
        id (int): Unique identifier for the user.
        email (str): User's email address.
        hashed_password (str): Hashed password for the user.
        session_id (str): Session ID for the user (optional).
        reset_token (str): Password reset token for the user (optional).
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(
        String(length=250),
        nullable=False,
    )
    hashed_password = Column(String(length=250), nullable=False)
    session_id = Column(String(length=250), nullable=True)
    reset_token = Column(String(length=250), nullable=True)

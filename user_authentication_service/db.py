#!/usr/bin/env python3


"""SQLAlchemy model for the 'users' table."""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from user import User

from user import Base


class DB:
    """
    Database class that handles database connections and operations.

    Attributes:
        _engine (Engine): SQLAlchemy engine object.
        __session (Session): SQLAlchemy session object.
    """

    def __init__(self):
        """
        Initializes the database engine and creates/drops tables.

        Creates a SQLite database engine with the `a.db`
        file and sets `echo=True` to enable database logging.
        Drops all existing tables and creates new ones
        based on the `Base` metadata.
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """
        Gets the current database session.

        If no session exists, creates a new one using the
        `sessionmaker` function and binds it to the database engine.

        Returns:
            Session: SQLAlchemy session object.
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Adds a new user to the database.

        Args:
            email (str): User's email address.
            hashed_password (str): Hashed password for the user.

        Returns:
            User: SQLAlchemy User object.
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user


my_db = DB()

user_1 = my_db.add_user("test@test.com", "SuperHashedPwd")
print(user_1.id)

user_2 = my_db.add_user("test1@test.com", "SuperHashedPwd1")
print(user_2.id)

#!/usr/bin/env python3


"""SQLAlchemy model for the 'users' table."""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound


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

    def find_user_by(self, **kwargs) -> User:
        """
        Finds a user in the database based on the provided keyword arguments.

        Args:
            **kwargs: Keyword arguments to filter the query.

        Returns:
            User: SQLAlchemy User object.
        """
        user = self._session.query(User).filter_by(**kwargs).first()
        if user is None:
            raise NoResultFound

        return user

     def update_user(self, user_id: int, **kwargs) -> None:
        """
        update_user.
        """
        session = self._session
        user = self.find_user_by(id=user_id)
        for k, v in kwargs.items():
            if k not in VALID_FIELDS:
                raise ValueError
            setattr(user, k, v)
        session.commit()
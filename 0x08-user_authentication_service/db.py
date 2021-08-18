#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import session
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """[summary]

        Args:
            email (str): [description]
            hashed_password (str): [description]

        Returns:
            User: [description]
        """
        user = User(email=email, hashed_password=hashed_password)
        session = self._session
        session.add(user)
        session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """[summary]

        Raises:
            InvalidRequestError: [description]
            NoResultFound: [description]

        Returns:
            User: [description]
        """
        for k in kwargs.keys():
            if k not in ["id", "email",
                         "hashed_password",
                         "session_id",
                         "reset_token"]:
                raise InvalidRequestError
        u = self._session.query(User).filter_by(**kwargs).first()
        if not u:
            raise NoResultFound
        return u

    def update_user(self, user_id: int, **kwargs) -> None:
        """[summary]

        Args:
            user_id (int): [description]

        Raises:
            ValueError: [description]

        Returns:
            [type]: [description]
        """
        user = self.find_user_by(id=user_id)
        for k, v in kwargs.items():
            if k not in user.__dict__.keys()\
                    or k == "_sa_instance_state":
                raise ValueError
            setattr(user, k, v)
        self._session.commit()
        return None

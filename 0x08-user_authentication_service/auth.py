#!/usr/bin/env python3
"""[Module]"""
import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """[summary]

    Args:
        password (str): [description]

    Returns:
        bytes: [description]
    """
    return bcrypt.hashpw(str.encode(password), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """[summary]

        Args:
            email (str): [description]
            password (str): [description]

        Returns:
            User: [description]
        """
        user = self._db.find_user_by(email=email)
        if user:
            raise ValueError(f'User ${email} already exists')
        hashed_password = _hash_password(password)
        return self._db.add_user(email, hashed_password)

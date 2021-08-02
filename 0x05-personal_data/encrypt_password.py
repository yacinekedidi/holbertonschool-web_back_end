#!/usr/bin/env python3
"""[Module]"""
import bcrypt
from typing import ByteString


def hash_password(password: str) -> ByteString:
    """[summary]

    Args:
        password (str): [description]

    Returns:
        ByteString: [description]
    """
    return bcrypt.hashpw(password, bcrypt.gensalt())

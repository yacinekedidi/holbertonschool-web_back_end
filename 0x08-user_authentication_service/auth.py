#!/usr/bin/env python3
"""[Module]"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """[summary]

    Args:
        password (str): [description]

    Returns:
        bytes: [description]
    """
    return bcrypt.hashpw(str.encode(password), bcrypt.gensalt())

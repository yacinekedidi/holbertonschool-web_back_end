#!/usr/bin/env python3
"""[Module]"""
import bcrypt


def hash_password(password: str) -> bytes:
    """[summary]
    """
    return bcrypt.hashpw(str.encode(password), bcrypt.gensalt())

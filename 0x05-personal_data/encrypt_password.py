#!/usr/bin/env python3
"""[Module]"""
from typing import ByteString
import bcrypt


def hash_password(password: str) -> ByteString:
    """[summary]
    """
    return bcrypt.hashpw(str.encode(password), bcrypt.gensalt())

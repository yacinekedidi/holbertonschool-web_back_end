#!/usr/bin/env python3
"""[Module]"""

from typing import Tuple
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """[summary]

    Args:
        Auth ([type]): [description]
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """[summary]

        Args:
            authorization_header (str): [description]

        Returns:
            str: [description]
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """[summary]

        Args:
            base64_authorization_header (str): [description]

        Returns:
            str: [description]
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            return base64.b64decode(
                base64_authorization_header).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
                self, decoded_base64_authorization_header:
                str) -> Tuple[str, str]:
        """[summary]

        Args:
            decoded_base64_authorization_header (str): [description]

        Returns:
            Tuple[str, str]: [description]
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) is not str:
            return None, None
        if decoded_base64_authorization_header.find(":") == -1:
            return None, None
        email, password = decoded_base64_authorization_header.split(":")
        return email, password

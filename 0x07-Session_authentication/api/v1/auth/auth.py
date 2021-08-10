#!/usr/bin/env python3
"""[Module]"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth():
    """[Class]
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """[summary]

        Args:
            path (str): [description]
            excluded_paths (List[str]): [description]

        Returns:
            bool: [description]
        """
        if path is None:
            return True
        if excluded_paths is None or not len(excluded_paths):
            return True
        path = f"{path}/" if path[-1] != '/' else path

        for index, p in enumerate(excluded_paths):
            if p[-1] != '/':
                excluded_paths[index] = f"{p}/"

            if excluded_paths[index].endswith('*/') and \
                    path.startswith(excluded_paths[index][:-2]):
                return False

        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """[summary]

        Args:
            request ([type], optional): [description]. Defaults to None.

        Returns:
            str: [description]
        """
        if request is None:
            return None
        try:
            return request.headers["Authorization"]
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """[summary]

        Returns:
            [type]: [description]
        """
        return None

    def session_cookie(self, request=None):
        """[summary]

        Args:
            request ([type], optional): [description]. Defaults to None.
        """
        if not request:
            return None
        session_name = getenv("SESSION_NAME")
        return request.cookies.get(session_name)

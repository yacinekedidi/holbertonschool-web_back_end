#!/usr/bin/env python3
"""[Module]"""
from flask import request
from typing import List, TypeVar


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
        if excluded_paths and path:
            excluded_paths = [f"{path}/" if path[-1] != '/'
                              else path for path in excluded_paths]
            path = f"{path}/" if path[-1] != '/' else path

        if path is None:
            return True
        if excluded_paths is None or not len(excluded_paths):
            return True
        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """[summary]

        Args:
            request ([type], optional): [description]. Defaults to None.

        Returns:
            str: [description]
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """[summary]

        Returns:
            [type]: [description]
        """
        return None

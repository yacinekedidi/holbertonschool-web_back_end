#!/usr/bin/env python3
"""[Module]"""
from flask.globals import session
from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """[summary]

    Args:
        Auth ([type]): [description]
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """[summary]

        Args:
            user_id (str, optional): [description]. Defaults to None.

        Returns:
            str: [description]
        """
        if not user_id or type(user_id) is not str:
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """[summary]

        Args:
            session_id (str, optional): [description]. Defaults to None.

        Returns:
            str: [description]
        """
        if not session_id or type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """[summary]

        Args:
            request ([type], optional): [description]. Defaults to None.
        """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        return User.get(user_id)

    def destroy_session(self, request=None):
        """[summary]

        Args:
            request ([type], optional): [description]. Defaults to None.
        """
        session_id = self.session_cookie(request)
        if not request or not session_id:
            return False
        user_id = self.user_id_for_session_id(session_id)
        if not user_id:
            return False
        del self.user_id_by_session_id[session_id]
        return True

#!/usr/bin/env python3
"""[Module]"""

from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, time, timedelta


class SessionExpAuth(SessionAuth):
    """[summary]

    Args:
        SessionAuth ([type]): [description]
    """
    def __init__(self):
        """[summary]
        """
        super().__init__()
        self.session_duration = int(getenv("SESSION_DURATION", 0))

    def create_session(self, user_id=None):
        """[summary]

        Args:
            user_id ([type], optional): [description]. Defaults to None.
        """
        try:
            session_id = super().create_session(user_id)
        except Exception:
            return None
        session_dictionary = {"user_id": user_id, "created_at": datetime.now()}
        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """[summary]

        Args:
            session_id ([type], optional): [description]. Defaults to None.
        """
        if not session_id or\
                session_id not in self.user_id_by_session_id.keys():
            return None
        if self.session_duration <= 0:
            return self.user_id_by_session_id[session_id].get("user_id")
        if "created_at" not in\
                self.user_id_by_session_id[session_id].keys():
            return None
        if timedelta(seconds=self.session_duration) +\
            self.user_id_by_session_id[session_id].get("created_at") <\
                datetime.now():
            return None
        return self.user_id_by_session_id[session_id].get("user_id")

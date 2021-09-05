#!/usr/bin/env python3
from typing import Callable, Optional, Union
import redis
import uuid
import sys


class Cache():
    """[Cache class]
    """
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """[summary]

        Args:
            data (Any): [description]

        Returns:
            str: [description]
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None)\
            -> Union[str, bytes, int, float]:
        """[summary]

        Returns:
            [type]: [description]
        """
        val = self._redis.get(key)
        if fn:
            return fn(val)
        return val

    def get_str(self, key: str):
        """[summary]

        Args:
            data (bytes): [description]

        Returns:
            [type]: [description]
        """
        return self.get(key, str)

    def get_int(self, key: int):
        """[summary]

        Args:
            data (bytes): [description]

        Returns:
            [type]: [description]
        """
        return self.get(key, int)

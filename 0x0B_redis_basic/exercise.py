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

    def get(self, key: str, fn: Optional[Callable])\
            -> Union[str, bytes, int, float]:
        """[summary]

        Returns:
            [type]: [description]
        """
        d = self._redis.get(key)
        if not fn:
            return d
        return fn(d)

    def get_str(self, data: bytes):
        """[summary]

        Args:
            data (bytes): [description]

        Returns:
            [type]: [description]
        """
        return data.decode("utf-8")

    def get_int(self, data: bytes):
        """[summary]

        Args:
            data (bytes): [description]

        Returns:
            [type]: [description]
        """
        return int.from_bytes(data, sys.byteorder)

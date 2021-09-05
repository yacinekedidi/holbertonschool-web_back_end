#!/usr/bin/env python3
from typing import Union
import redis
import uuid


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

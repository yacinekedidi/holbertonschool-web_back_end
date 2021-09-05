#!/usr/bin/env python3
from functools import wraps
from typing import Callable, Optional, Union
import redis
import uuid


def count_calls(method: Callable) -> Callable:
    """[summary]

    Args:
        method (Callable): [description]

    Returns:
        Callable: [description]
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """[wrapper]

        Returns:
            [type]: [description]
        """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """[summary]

    Args:
        method (Callable): [description]

    Returns:
        Callable: [description]
    """
    @wraps(method)
    def wrapper(self, *args):
        """[summary]

        Returns:
            [type]: [description]
        """
        self._redis.rpush(f"{method.__qualname__}:inputs", str(args))
        key = method(self, *args)
        self._redis.rpush(f"{method.__qualname__}:outputs", str(key))
        return key
    return wrapper


def replay(method: Callable) -> Callable:
    method_name = method.__qualname__
    inputs_key = f"{method_name}:inputs"
    outputs_key = f"{method_name}:outputs"
    r = method.__self__._redis
    counts = r.get(method_name)
    print(f"{method_name} was called {int(counts)} times")

    inputs = r.lrange(inputs_key, 0, -1)
    outputs = r.lrange(outputs_key, 0, -1)
    for inp, out in zip(inputs, outputs):
        print(
            f"{method_name}(*{inp.decode('utf-8')}) -> {out.decode('utf-8')}")


class Cache():
    """[Cache class]
    """
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
            key (str): [description]

        Returns:
            [type]: [description]
        """
        return self.get(key, str)

    def get_int(self, key: int):
        """[summary]

        Args:
            key (int): [description]

        Returns:
            [type]: [description]
        """
        return self.get(key, int)

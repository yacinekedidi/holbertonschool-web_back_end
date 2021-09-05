#!/usr/bin/env python3
"""[summary]"""
import requests
import redis
from functools import wraps
from typing import Callable
r = redis.Redis()


def count(method: Callable) -> Callable:
    """[summary]

    Args:
        method (Callable): [description]

    Returns:
        Callable: [description]
    """
    @wraps(method)
    def wrapper(url):
        """[summary]

        Args:
            url ([type]): [description]

        Returns:
            [type]: [description]
        """
        stored = r.get(f"result:{url}")
        if stored:
            return stored.decode("utf-8")
        r.incr(f"count:{url}")
        html = method(url)
        r.setex(f"result:{url}", 10, html)
        return html
    return wrapper


@count
def get_page(url: str) -> str:
    """[summary]

    Args:
        url (str): [description]

    Returns:
        str: [description]
    """
    return requests.get(url).text

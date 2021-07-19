#!/usr/bin/env python3
"""[summary]"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """[summary]

    Args:
        k (str): [a string]
        v (Union[int, float]): [either an int or a float]

    Returns:
        Tuple: [The first element of the tuple is the string k.
        The second element is the square of the int/float v
        and should be annotated as a float.]
    """
    return (k, v ** 2)

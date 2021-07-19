#!/usr/bin/env python3
"""[summary]"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """[summary]

    Args:
        multiplier (float): [a float]

    Returns:
        Callable[[float], float]: [a function that
        multiplies multiplier by a float]
    """
    return lambda m: m * multiplier

#!/usr/bin/env python3
"""[a module containing a coroutine function]"""
from typing import Callable, Generator, List
async_generator: Callable[[None], Generator[float, None, None]] =\
    __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """[collect 10 random numbers using
    an async comprehensing over async_generator,
    then return the 10 random numbers.]

    Returns:
        List[float]: [list of 10 random numbers]
    """
    return [random_num async for random_num in async_generator()]

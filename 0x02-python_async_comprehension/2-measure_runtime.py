#!/usr/bin/env python3
"""[summary]"""
import asyncio
import time
from typing import Callable, List
async_comprehension: Callable[[], List[float]] =\
    __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """[Run time for four parallel comprehensions]

    Returns:
        float: [return the time it took
        for four parallel comprehensions]
    """
    s = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.perf_counter() - s

#!/usr/bin/env python3
"""[summary]"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """[summary]

    Args:
        n (int): [description]
        max_delay (int): [description]

    Returns:
        float: [description]
    """
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - s
    return elapsed / n

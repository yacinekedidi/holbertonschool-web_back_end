#!/usr/bin/env python3
"""[summary]"""
import asyncio
from typing import Callable, List
task_wait_random: Callable[[int], List[float]] =\
    __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """[summary]

    Args:
        n (int): [description]
        max_delay (int): [description]

    Returns:
        List[float]: [description]
    """
    delays_list = [await task_wait_random(max_delay) for i in range(n)]
    return sorted(delays_list)

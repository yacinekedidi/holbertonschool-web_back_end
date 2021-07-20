#!/usr/bin/env python3
"""[summary]"""
import asyncio
from typing import Callable
wait_random: Callable[[int], float]\
    = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """[summary]

    Args:
        max_delay (int): [description]

    Returns:
        asyncio.Task: [description]
    """
    return asyncio.create_task(wait_random(max_delay))

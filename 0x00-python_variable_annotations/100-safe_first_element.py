#!/usr/bin/env python3
"""[summary]"""
from typing import Optional, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """[summary]

    Args:
        lst (Sequence[Any]): [sequence on any types]

    Returns:
        Optional[Any]: [equivalent to Union[Any, None]]
        which means could return either any type or none
    """
    if lst:
        return lst[0]
    else:
        return None

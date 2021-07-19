#!/usr/bin/env python3
"""[summary]"""
from typing import Tuple, List, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """[summary]

    Args:
        lst (List[Any]): [description]
        factor (int, optional): [description]. Defaults to 2.

    Returns:
        List[Any]: [description]
    """
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), 3)

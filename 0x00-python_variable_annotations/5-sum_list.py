#!/usr/bin/env python3
"""[a simple modyule containing]"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """[takes a list input_list of floats as argument
    and returns their sum as a float.]

    Args:
        input_list (List[float]): [list of floats]

    Returns:
        float: [sum of the list of floats]
    """
    return sum(input_list)

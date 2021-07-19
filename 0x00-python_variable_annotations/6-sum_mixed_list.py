#!/usr/bin/env python3
"""[summary]"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """[summary]

    Args:
        mxd_lst (List[int, float]): [list of integers and floats]

    Returns:
        float: [sum of the mxd_lst]
    """
    return sum(mxd_lst)

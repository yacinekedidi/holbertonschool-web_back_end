#!/usr/bin/env python3
"""[summary]"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """[ takes a list mxd_lst of integers and floats
    and returns their sum as a float.]

    Args:
        mxd_lst (List[int, float]): [list of integers and floats]

    Returns:
        float: [sum of the mxd_lst]
    """
    return sum(mxd_lst)

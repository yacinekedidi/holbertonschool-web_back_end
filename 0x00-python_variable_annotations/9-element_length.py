#!/usr/bin/env python3
"""[summary]"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """[summary]

    Args:
        lst (Iterable[Sequence]): [iterables of sequences]

    Returns:
        List[Tuple[Sequence, int]]:
        [list of tuples containing
        as first element a sequence
        and as second element an int]
    """
    return [(i, len(i)) for i in lst]

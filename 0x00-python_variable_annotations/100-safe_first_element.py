#!/usr/bin/env python3
"""[summary]"""
from typing import Optional, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    if lst:
        return lst[0]
    else:
        return None

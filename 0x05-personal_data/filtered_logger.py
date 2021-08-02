#!/usr/bin/env python3
"""[filtered_logger Module]"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """[summary]

    Args:
        fields (List[str]): [description]
        redaction (str): [description]
        message (str): [description]
        separator (str): [description]

    Returns:
        str: [description]
    """
    return (
        ';'.join(
            re.sub('=.*', f"={redaction}", i)
            if i.split('=')[0] in fields
            else i
            for i in message.split(separator)[:-1]
        )
        + ';'
    )

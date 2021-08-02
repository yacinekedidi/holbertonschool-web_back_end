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
    msg_list = message.split(separator)
    for c, i in enumerate(msg_list):
        try:
            msg_list[c] = re.sub(i[i.index('=') + 1:], redaction, i)\
                if i[:i.index('=')] in fields else i
        except ValueError:
            pass
    return ';'.join(msg_list)

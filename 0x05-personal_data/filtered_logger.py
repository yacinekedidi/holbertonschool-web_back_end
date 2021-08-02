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
    msg_list = message.split(separator)[:-1]
    for c, i in enumerate(msg_list):
        msg_list[c] = re.sub(i.split('=')[1], redaction, i)\
            if i.split('=')[0] in fields else i
    return ';'.join(msg_list) + ';'

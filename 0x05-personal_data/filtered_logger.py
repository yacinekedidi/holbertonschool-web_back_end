#!/usr/bin/env python3
"""[filtered_logger Module]"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """[summary]

    Args:
        fields (List[str]): [representing all fields to obfuscate]
        redaction (str): [representing by what the field will be obfuscated]
        message (str): [representing the log line]
        separator (str): [ representing by which character is separating
        all fields in the log line]

    Returns:
        str: [the log message obfuscated:]
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

#!/usr/bin/env python3
"""[filtered_logger Module]"""
from typing import List
import re
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        """[summary]

        Args:
            fields ([type]): [description]
        """
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """[summary]

        Args:
            record (logging.LogRecord): [description]

        Returns:
            str: [description]
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


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
    for f in fields:
        message = re.sub(f'{f}=.*?{separator}', f"{f}={redaction}{separator}",
                         message)
    return message

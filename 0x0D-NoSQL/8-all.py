#!/usr/bin/env python3
"""Module"""


def list_all(mongo_collection):
    """[summary]

    Args:
        mongo_collection ([type]): [description]

    Returns:
        [type]: [description]
    """
    if not mongo_collection:
        return []
    return mongo_collection.find()

#!/usr/bin/env python3
"""[Module]"""


def insert_school(mongo_collection, **kwargs):
    """[summary]

    Args:
        mongo_collection ([type]): [description]

    Returns:
        [type]: [description]
    """
    res = mongo_collection.insert_one(kwargs)
    return res.inserted_id

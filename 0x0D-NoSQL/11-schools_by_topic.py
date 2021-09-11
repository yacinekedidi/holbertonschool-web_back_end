#!/usr/bin/env python3
"""Module"""


def schools_by_topic(mongo_collection, topic):
    """[summary]

    Args:
        mongo_collection ([type]): [description]
        topic ([type]): [description]

    Returns:
        [type]: [description]
    """
    return mongo_collection.find({"topics": topic})

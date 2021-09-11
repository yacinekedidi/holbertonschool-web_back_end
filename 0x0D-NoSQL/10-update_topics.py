#!/usr/bin/env python3
"""Module"""


from typing import List


def update_topics(mongo_collection, name: str, topics: List):
    """[summary]

    Args:
        mongo_collection ([type]): [description]
        name ([type]): [description]
        topics ([type]): [description]
    """
    mongo_collection.update_many({"name": name},
                                 {"$set": {"topics": topics}})

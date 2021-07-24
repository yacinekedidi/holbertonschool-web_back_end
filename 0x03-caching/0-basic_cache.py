#!/usr/bin/env python3
""""Module"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """[summary]

    Args:
        BaseCaching ([type]): [description]
    """
    def __init__(self):
        """[summary]
        """
        super().__init__()

    def put(self, key, item):
        """[summary]

        Args:
            key ([type]): [description]
            item ([type]): [description]
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """[summary]

        Args:
            key ([type]): [description]
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]

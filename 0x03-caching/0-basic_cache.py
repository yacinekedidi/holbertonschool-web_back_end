#!/usr/bin/env python3
""""BasicCache Module"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """[basic cache strategy]

    Args:
        BaseCaching ([class]): [parent]
    """
    def __init__(self):
        """[constructor]
        """
        super().__init__()

    def put(self, key, item):
        """[- assign to the dictionary self.cache_data the item value
            for the key @key.
            - If key or item is None, this method should not do anything.]

        Args:
            key ([Any]): [@self.cache_data key]
            item ([type]): [new value]
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """[- Must return the value in self.cache_data linked to key.
            - If key is None or if the key doesn’t exist in self.cache_data,
            return None.]

        Args:
            key ([Any]): [@self.cache_data key]

        Returns:
            [Any]: [the value in self.cache_data linked to key.]
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]

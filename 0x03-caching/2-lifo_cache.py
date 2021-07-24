#!/usr/bin/env python3
"""LIFOCache Module"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """[LIFO caching system]

    Args:
        BaseCaching ([class]): [parent class]
    """
    def __init__(self):
        """[summary]
        """
        super().__init__()

    def put(self, key, item):
        """[
            - Must assign to the dictionary self.cache_data the item value
            for the key key.
            - if key or item is None, this method should not do anything.
            - If the number of items in self.cache_data is higher that
            BaseCaching.MAX_ITEMS:
                -  must discard the last item put in cache (LIFO algorithm)
                -  must print DISCARD: with the key discarded and following by
                a new line]

        Args:
            key ([Any]): [dictionary's key]
            item ([Any]): [dictionary's value]
        """
        if key is None or item is None:
            return
        keys_list = self.cache_data.keys()
        if len(keys_list) == super().MAX_ITEMS:
            if key in keys_list:
                del self.cache_data[key]
            else:
                last_key = list(keys_list)[-1]
                print(f'DISCARD: {last_key}')
                del self.cache_data[last_key]
        self.cache_data[key] = item

    def get(self, key):
        """[gets the value for the requested key]

        Args:
            key ([Any]): [description]

        Returns:
            [Any]: [the value in self.cache_data linked to key]
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]

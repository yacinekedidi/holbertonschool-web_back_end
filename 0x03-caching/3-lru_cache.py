#!/usr/bin/env python3
"""[LRUCache module]"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """[summary]

    Args:
        BaseCaching ([type]): [description]
    """
    def __init__(self):
        super().__init__()
        self.LRU_list = [i for i in range(super().MAX_ITEMS)]

    def put(self, key, item):
        """[summary]

        Args:
            key ([type]): [description]
            item ([type]): [description]
        """
        if key is None or item is None:
            return
        keys_list = list(self.cache_data.keys())
        if len(keys_list) == super().MAX_ITEMS:
            if key in keys_list:
                self.LRU_list[keys_list.index(key)] = max(self.LRU_list) + 1
            else:
                k = self.LRU_list.index(min(self.LRU_list))
                print(f"DISCARD: {keys_list[k]}")
                del self.cache_data[keys_list[k]]
                del self.LRU_list[k]
                self.LRU_list.append(max(self.LRU_list) + 1)
        self.cache_data[key] = item

    def get(self, key):
        """[summary]

        Args:
            key ([type]): [description]

        Returns:
            [type]: [description]
        """
        if key is None or key not in self.cache_data.keys():
            return None
        keys_list = list(self.cache_data.keys())
        self.LRU_list[keys_list.index(key)] = max(self.LRU_list) + 1
        return self.cache_data[key]

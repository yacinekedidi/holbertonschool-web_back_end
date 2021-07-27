#!/usr/bin/env python3
"""[MRUCache module]"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """[summary]

    Args:
        BaseCaching ([type]): [description]
    """
    def __init__(self):
        super().__init__()
        self.MRU_list = [i for i in range(super().MAX_ITEMS)]

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
                self.MRU_list[keys_list.index(key)] = max(self.MRU_list) + 1
            else:
                k = self.MRU_list.index(max(self.MRU_list))
                print(f"DISCARD: {keys_list[k]}")
                del self.cache_data[keys_list[k]]
                del self.MRU_list[k]
                self.MRU_list.append(max(self.MRU_list) + 1
                                     if len(self.MRU_list) > 0 else 0)
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
        self.MRU_list[keys_list.index(key)] = max(self.MRU_list) + 1
        return self.cache_data[key]

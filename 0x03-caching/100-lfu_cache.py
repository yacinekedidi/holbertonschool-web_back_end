#!/usr/bin/env python3
"""[LFUCache module]"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """[summary]

    Args:
        BaseCaching ([type]): [description]
    """
    def __init__(self):
        super().__init__()
        self.LFU_list = [0 for _ in range(super().MAX_ITEMS)]

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
                self.LFU_list[keys_list.index(key)] += 1
            else:
                k = self.LFU_list.index(min(self.LFU_list))
                print(f"DISCARD: {keys_list[k]}")
                del self.cache_data[keys_list[k]]
                del self.LFU_list[k]
                self.LFU_list.append(1)
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
        self.LFU_list[keys_list.index(key)] += 1
        return self.cache_data[key]

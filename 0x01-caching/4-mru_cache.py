#!/usr/bin/env python3
"""
MRUCache module
"""

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """ MRUCache implements:
      - the put and get methods as most recently used
    """
    def __init__(self):
        """
        This is intializing functionality from parent class
        """
        super().__init__()
        self.mru_keys = []

    def put(self, key, item):
        """
        Adds an item to the cache dict
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key in self.mru_keys:
                self.mru_keys.remove(key)

            if len(self.cache_data) > self.MAX_ITEMS:
                rem = self.mru_keys.pop()
                del self.cache_data[rem]
                print("DISCARD: {}".format(rem))

            self.mru_keys.append(key)


    def get(self, key):
        """
        Retrives the item
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)

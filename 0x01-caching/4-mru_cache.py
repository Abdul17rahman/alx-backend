#!/usr/bin/env python3
"""
MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache implements:
      - the put and get methods as last-in first-out
    """
    def __init__(self):
        """
        This is intializing functionality from parent class
        """
        super().__init__()

    def put(self, key, item):
        """
        Adds an item to the cache dict
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = self.cache_data.pop(key)
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                itm, _ = self.cache_data.popitem()
                print("DISCARD: {}".format(itm))
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrives the item
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)

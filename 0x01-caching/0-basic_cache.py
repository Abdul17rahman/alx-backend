#!/usr/bin/env python3
"""
Basic cache class
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BaseCache implements:
      - the put and get methods
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
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrives the item
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)

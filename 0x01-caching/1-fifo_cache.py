#!/usr/bin/env python3
"""
FIFOCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache implements:
      - the put and get methods as first-in first-out
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
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                itm = next(iter(self.cache_data))
                print("DISCARD: {}".format(itm))
                del self.cache_data[itm]
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrives the item
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)

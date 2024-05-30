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
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Adds an item to the cache dict
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.move_to_end(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru, _ = self.cache_data.popitem(last=True)
                print("DISCARD: {}".format(mru))
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrives the item
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)

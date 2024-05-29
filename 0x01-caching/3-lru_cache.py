#!/usr/bin/env python3
"""
LRUCache module
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ LRUCache implements:
      - the put and get methods as least recently used
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
                self.cache_data.pop(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru, _ = self.cache_data.popitem(last=False)
                print("DISCARD: {}".format(lru))
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrives the item
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)

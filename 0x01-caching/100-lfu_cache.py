#!/usr/bin/env python3
"""
LFUCache module
"""

from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """ LFUCache implements:
      - the put and get methods with Least Frequently Used
    """
    def __init__(self):
        """
        Initialize the class using the parent class initializer
        """
        super().__init__()
        self.frequency = defaultdict(int)  # To count the frequency of accesses
        self.usage_order = {}  # To maintain the usage order for LRU
        self.time = 0  # A simple counter to keep track of the order of usage

    def put(self, key, item):
        """
        Add an item to the cache.If cache exceeds the maximum allowed items,
        discard the least frequently used item. If there is a tie, discard the
        least recently used one.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    # Find the least frequently used item
                    lfu_key = min(self.frequency, key=lambda k:
                                  (self.frequency[k], self.usage_order[k]))
                    del self.cache_data[lfu_key]
                    del self.frequency[lfu_key]
                    del self.usage_order[lfu_key]
                    print("DISCARD: {}".format(lfu_key))
            # Update the cache with the new item
            self.cache_data[key] = item
            self.frequency[key] = self.frequency.get(key, 0) + 1
            self.usage_order[key] = self.time
            self.time += 1

    def get(self, key):
        """
        Get an item by key and update its frequency and usage order
        """
        if key is None or key not in self.cache_data:
            return None
        self.frequency[key] += 1
        self.usage_order[key] = self.time
        self.time += 1
        return self.cache_data.get(key)

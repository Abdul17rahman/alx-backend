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
        super()

    def put(self, key, item):
        pass

    def get(self, key):
        pass
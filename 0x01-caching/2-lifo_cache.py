#!/usr/bin/env python3
"""This module creates a class LIFOCache that inherits from BaseCaching and is a caching system
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """This allows items to be stored and
    retrieved from a dictionary with a LIFO
    removal principle when the limit is reached.
    """
    def __init__(self):
        """This initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """This adds an item in the cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)

#!/usr/bin/env python3
"""This module creates a class named BasicCache that inherits from BaseCaching and is a caching system.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """This is an object that allows storing and
    retrieving items from a dictionary.
    """
    def put(self, key, item):
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """This retrieves an item by key.
        """
        return self.cache_data.get(key, None)

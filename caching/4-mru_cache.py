#!/usr/bin/env python3


"""MRU caching module"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache defines:
    - constants of your caching system
    - where your data are stored (in a dictionary)
    """

    def __init__(self):
        """Initiliaze"""
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key in self.cache_data:
                self.cache_data.pop(key)
            else:
                itemss = self.cache_data.popitem()
                print("DISCARD: {}".format(itemss[0]))
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        value = self.cache_data.pop(key)
        self.cache_data[key] = value
        return value

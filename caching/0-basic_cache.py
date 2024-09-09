#!/usr/bin/env python3

"""BasicCache defines:"""
import importlib

BaseCaching = importlib.import_module("base_caching").BaseCaching
"""BasicCache class defines:
- constants of your caching system
- where your data are stored (in a dictionary)
"""


class BasicCache(BaseCaching):
    """BasicCache defines:
    - constants of your caching system
    - where your data are stored (in a dictionary)
    """

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)

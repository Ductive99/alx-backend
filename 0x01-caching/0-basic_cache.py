#!/usr/bin/env python3
"""Task 0 - BasicCache
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Caching System Class
    - adds an item to the cache
    - returns an item from a given key
    """
    def put(self, key, item):
        """adds an item to the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """returns the item based on the key
        """
        return self.cache_data.get(key, None)

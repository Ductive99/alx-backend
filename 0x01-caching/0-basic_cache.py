#!/usr/bin/env python3
"""Task 0
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Caching System Class
    """
    def put(self, key, item):
        """adds a item to the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """returns the item based on the key
        """
        return self.cache_data.get(key, None)

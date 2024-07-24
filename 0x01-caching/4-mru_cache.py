#!/usr/bin/env python3
"""MRUCache module."""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    A class that allows storing and
    retrieving items from a dictionary with an MRU
    removal mechanism when the limit is reached.
    """

    def __init__(self):
        """Initialize the cache."""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Adds an item in the cache."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded = self.order.pop()
            del self.cache_data[discarded]
            print(f"DISCARD: {discarded}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Retrieves an item by key."""
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]

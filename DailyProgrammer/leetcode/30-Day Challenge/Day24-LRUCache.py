# -*- coding: utf-8 -*-
"""
Design and implement a data structure for Least Recently Used (LRU) cache. It 
should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists
in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. 
When the cache reached its capacity, it should invalidate the least recently 
used item before inserting a new item.

The cache is initialized with a positive capacity.
"""

class LRUCache:

    def __init__(self, capacity: int):
        
        self.capacity = capacity
        self.capMap = {}

    def get(self, key: int) -> int:        
        if key not in self.capMap:
            return -1
        else:
            placeholder = self.capMap[key]
            del self.capMap[key]
            self.capMap[key] = placeholder
            return self.capMap[key]

    def put(self, key: int, value: int) -> None:
        
        if key not in self.capMap:
            self.capMap[key] = value
            if len(self.capMap) > self.capacity:
                for dictKey in self.capMap:
                    del self.capMap[dictKey]
                    break
        
        else:
            del self.capMap[key]
            self.capMap[key] = value
            return None

# hash_table.py
# implementation of simple hash table
# we'll use separate chaining with Python's built-in 
# list type acting as the chains
# Strongly suggest you turn off LLMs like
# GitHub Copilot, TabNine, etc. when working on this file.
# Writing a data structure yourself is the best
# way to learn how it works.
# by: Harris Adam
from random import randint

class HashTable:
    MAX_LOAD_FACTOR = 0.7
    GROWTH_FACTOR = 2

    def __init__(self, slots = 10):
        self.slots = slots
        self.num_items = 0
        self.backing_store = [[] for _ in range(slots)]

    def _hash(self, key):
        return hash(key) % self.slots

    # insert a new key-value pair into the 
    # hash table or if the key is already present
    # update its associated value
    # make sure to resize if MAX_LOAD_FACTOR is exceeded
    def insert(self, key, value):
        chain = self.backing_store[self._hash(key)]
        for i, (k, _) in enumerate(chain):
            if k == key:
                chain[i] = (key, value)
                return
        chain.append((key, value))
        self.num_items += 1
        if self.num_items / self.slots > self.MAX_LOAD_FACTOR:
            self._resize()

    # return the value associated with the key
    def get(self, key):
        for k, v in self.backing_store[self._hash(key)]:
            if k == key:
                return v
        return None

    # eliminate the key-value pair associated with key
    def remove(self, key):
        chain = self.backing_store[self._hash(key)]
        for i, (k, _) in enumerate(chain):
            if k == key:
                del chain[i]
                self.num_items -= 1
                return True
        return False
    
    # update the hash table based on GROWTH_FACTOR
    # make sure to move everything over to the new table
    def _resize(self):
        old_store = self.backing_store
        self.slots = self.slots * self.GROWTH_FACTOR
        self.backing_store = [[] for _ in range(self.slots)]
        for chain in old_store:
            for key, value in chain:
                self.backing_store[self._hash(key)].append((key, value))

    def __str__(self):
        return str(self.backing_store)

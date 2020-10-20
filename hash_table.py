# HashTable: An unordered key-value data structure providing O(1) store, retrieve
# search and delete operations.
# Your implementation should pass the tests in test_hash_table.py.
# YOUR NAME


class HashTable:

    def init(self, capacity=10):
        self.data = []
        self.capacity = capacity

    def size(self):
        self.data = [[] for i in range(self.capacity)]
        return self.capacity

    def setitem(self, key, value):
        hash_index = self.hash(key)
        self.data[hash_index].append([key, value])

    def hash(self, input):
        return hash(input)
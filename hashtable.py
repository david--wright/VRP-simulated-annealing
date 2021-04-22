#! /usr/bin/env python3

class HashTable():
    def __init__(self, initalSize):
        self.table = [[] for _ in range(initalSize)]
        self.size = 0
    
    # def __delete__(self, instance):

    def __iter__(self):
        for bucket in self.table:
            for element in bucket:
                yield element[0]

    def __getitem__(self, key):
        hash_key = self.hash(key)
        bucket = self.table[hash_key]
        index = [item[0] for item in bucket].index(key)
        return bucket[index][1] 

    def __setitem__(self, key, value):
        hash_key = self.hash(key)
        bucket = self.table[hash_key]
        try:
            index = [item[0] for item in bucket].index(key)
            bucket[index] = (key,value)
        except ValueError:
            bucket.append((key,value))
            self.size += 1

    def __len__(self):
        return self.size
    
    def hash(self, key):
        return hash(key) % len(self.table)

    def items(self):
        for bucket in self.table:
            for element in bucket:
                yield element

    def values(self):
        for bucket in self.table:
            for element in bucket:
                yield element[1]
    
    def pop(key):
        hash_key = self.hash(key)
        bucket = self.table[hash_key]
        try:
            index = [item[0] for item in bucket].index(key)
            bucket.pop(index)
            self.size -= 1     
        except ValueError:
            return None
    



    

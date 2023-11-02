class HashTable:
    def __init__(self, size = 100):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.size

    def set(self, key, value):
        hash_key = self._hash(key)
        key_value = [key, value]

        for i, pair in enumerate(self.table[hash_key]):
            if pair[0] == key:
                self.table[hash_key][i] = key_value
            return
        self.table[hash_key].append(key_value)


    def get(self, key):
        hash_key = self._hash(key)
        if len(self.table[hash_key]) != 0:
            for pair in self.table[hash_key]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        hash_key = self._hash(key)
        removed = filter(lambda pair: pair[0] != key, self.table[hash_key])
        self.table[hash_key] = list(removed)
        return True if removed else False

    
ht = HashTable()
ht.set('Столи', 6)
ht.set('Комоди', 12)
ht.set('Дивани', 24)

class HashTable:
    def __init__(self, capacity, load_factor_threshold=0.7, resize_factor=2):
        self.capacity = capacity
        self.load_factor_threshold = load_factor_threshold
        self.resize_factor = resize_factor
        self.size = 0
        self.values = capacity * [None]

    #return hashtable length
    def __len__(self):
        return len(self.values)

    #remove item from hashtable if it exists and reduce size
    def __delitem__(self, key):
        if key in self:
            self[key] = None
            self.size -= 1
        else:
            raise KeyError(key)

    #set key value pair in hash table, increase size if it's not a delete operation (value = None)
    def __setitem__(self, key, value):
        if self.size >= self.load_factor_threshold * self.capacity:
            self._resize()
        self.values[self._index(key)] = value
        if value != None:
            self.size += 1

    #return value at specified key
    def __getitem__(self, key):
        value = self.values[self._index(key)]
        return value

    #check if key exists in hash table
    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True

    #iterate through values in hash table
    def __iter__(self):
        for value in self.values:
            if value is not [None]:
                yield value

    #return index of key
    def _index(self, key):
        return hash(key) % len(self)

    #when size >= capacity * resize factor, create new hash table with double capacity and write key/value pairs to it
    def _resize(self):
        new_capacity = self.capacity * self.resize_factor
        new_values = new_capacity * [None]
        for key, value in self.items():
            new_index = hash(key) % new_capacity
            new_values[new_index] = value
        self.capacity = new_capacity
        self.values = new_values

    #iterate through key value pairs
    def items(self):
        for i in range(len(self.values)):
            if self.values[i] is not None:
                yield (i, self.values[i])
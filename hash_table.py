class HashTable:
    def __init__(self, capacity, load_factor_threshold=0.7, resize_factor=2):
        self.capacity = capacity
        self.load_factor_threshold = load_factor_threshold
        self.resize_factor = resize_factor
        self.size = 0
        self.values = capacity * [None]

    def __len__(self):
        return len(self.values)

    def __delitem__(self, key):
        if key in self:
            self[key] = None
            self.size -= 1
        else:
            raise KeyError(key)

    def __setitem__(self, key, value):
        if self.size >= self.load_factor_threshold * self.capacity:
            self._resize()
        self.values[self._index(key)] = value
        self.size += 1

    def __getitem__(self, key):
        value = self.values[self._index(key)]
        return value
        # try:
        #     self[key]
        # except KeyError:
        #     return False
        # else:
        #     return True


    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True

    def __iter__(self):
        for value in self.values:
            if value is not [None]:
                yield value

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def _index(self, key):
        return hash(key) % len(self)
    
    def _resize(self):
        new_capacity = self.capacity * self.resize_factor
        new_values = new_capacity * [None]
        for value, key in self.items():
            new_index = hash(key) % new_capacity
            new_values[new_index] = value
        self.capacity = new_capacity
        self.values = new_values

    def items(self):
        for i in range(len(self.values)):
            if self.values[i] is not None:
                yield (self.values[i], i)
class HashMap:
    def __init__(self):
        self._size = 0
        self._capacity = 7
        self.table = {}
    
    def hash_function(self, r, c, rows):
        '''
        hash human pyramid so the keys are the (r, c) and
        the values is the weight borne by that person
        '''
        return (r * rows + c)

    def get(self, key):
        if key not in self.table:
            raise KeyError("Key was not found")
        return self.table[key]

    def set(self, key, value):
        self.table[key] = value
        self._size += 1
        if (self._size / self._capacity >= 0.8):
            self.resize()
        
    def resize(self):
        self._capacity = ((2 * self._capacity) - 1)
        new_table = {}
        for key, value in self.table.items():
            new_table[key] = value
        self.table = new_table

    def remove(self, key):
        if key in self.table:
            del self.table[key]
            self._size -= 1

    def clear(self):
        self._size = 0
        self.table.clear()

    def size(self):
        return self._size

    def capacity(self):
        return self._capacity
    
    def keys(self):
        return list(self.table.keys())


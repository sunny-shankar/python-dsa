class HashTable:

  def __init__(self):
    self.MAX = 100
    self.arr = [None for i in range(self.MAX)]

  def get_hash(self, key):
    sum = 0
    for char in key:
      sum += ord(char)
    return sum % self.MAX

  def insert(self, index, value):
    hash = self.get_hash(index)
    self.arr[hash] = value

  def get(self, index):
    hash = self.get_hash(index)
    return self.arr[hash]

  def delete(self, index):
    hash = self.get_hash(index)
    del self.arr[hash]


h = HashTable()

class HashTable:

  def __init__(self):
    self.MAX = 10
    self.arr = [[] for i in range(self.MAX)]

  def get_hash(self, key):
    sum = 0
    for char in key:
      sum += ord(char)
    return sum % self.MAX

  def insert(self, index, value):
    hash = self.get_hash(index)
    found = False
    for idx, data in enumerate(self.arr[hash]):
      if len(data) == 2 and data[0] == index:
        self.arr[hash][idx] = (index, value)
        found = True
    if not found:
      self.arr[hash].append((index, value))

  def get(self, index):
    hash = self.get_hash(index)
    for value in self.arr[hash]:
      if value[0] == index:
        return value[1]

  def delete(self, index):
    hash = self.get_hash(index)
    del self.arr[hash]
    for idx,value in enumerate(self.arr[hash]):
      if value[0] == index:
        del self.arr[hash][idx]
        

h = HashTable()

h.insert("march 6", 132435400)

h.insert("march 17", 100)

res = h.get("march 6")

print(res)
print(h.get("march 17"))

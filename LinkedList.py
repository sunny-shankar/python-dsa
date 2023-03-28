class Node:

  def __init__(self, value, next=None):
    self.value = value
    self.next = next


class LinkedList:

  def __init__(self):
    self.head = None

  def insert_at_start(self, value):
    current = self.head
    self.head = Node(value, current)

  def insert_at_end(self, value):
    current = self.head
    while current.next:
      current = current.next
    current.next = Node(value)

  def insert_at(self, index, value):
    current = self.head
    if index == 0:
      self.insert_at_start(value)
    for i in range(index):
      current = current.next
    current.next = Node(value, current.next.next)

  def get_length(self):
    current = self.head
    count = 0
    while current:
      count += 1
      current = current.next
    # print(count)
    return count

  def delete_node(self, index):
    current = self.head
    if index < 0 or index > self.get_length():
      print("index not found")
      return
    if index == 0:
      self.head = current.next
      return
    for i in range(index - 1):
      current = current.next
    current.next = current.next.next

  def print(self):
    current = self.head

    while current:
      print(current.value, end=" -> ")
      current = current.next
    print()

  def search(self, key):
    current = self.head
    count = 0
    while current:
      if current.value == key:
        print(f"fount at index {count}")
        return count
      count += 1
      current = current.next
    return "Not Found"

  def bubbleSort(self):
    current = self.head
    index = Node(None)

    while current:
      index = current.next

      while index:
        if current.value > index.value:
          current.value, index.value = index.value, current.value
        index = index.next

      current = current.next


if __name__ == '__main__':
  list = LinkedList()
  list.insert_at_start(1)
  list.insert_at_start(2)
  list.insert_at_start(3)
  list.insert_at_start(4)
  list.insert_at_end(500)
  list.insert_at(1, 100)
  list.print()
  # list.search(100)
  list.bubbleSort()
  # list.delete_node(4)
  list.print()

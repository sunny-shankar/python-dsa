class Node:

  def __init__(self, value, next=None, prev=None):
    self.value = value
    self.next = next
    self.prev = prev


class DoubleLinkedList:

  def __init__(self):
    self.head = None

  def insert_at_start(self, value):
    current = self.head
    self.head = Node(value, current)

  def print(self):
    current = self.head
    while current:
      print(current.value, end=" ")
      current = current.next

    print()

  def insert_at(self, index, value):
    current = self.head
    count = 0
    while current:
      if count == index - 1:
        current.next = Node(value, current.next, current)

      count += 1
      current = current.next


dl = DoubleLinkedList()

dl.insert_at_start(1)
dl.insert_at_start(2)
dl.insert_at_start(3)

dl.insert_at(1, 13)
dl.insert_at(4, 1000)
dl.insert_at(1, 1300)

dl.print()

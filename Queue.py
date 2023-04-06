from collections import deque


class Queue:

  def __init__(self):
    self.queue = deque()

  def enqueue(self, value):
    self.queue.appendleft(value)

  def dequeue(self):
    if not self.is_empty():
      return self.queue.pop()
    return ""

  def is_empty(self):
    return len(self.queue) == 0

  def length(self):
    return len(self.queue)


if __name__ == "__main__":
  qe = Queue()
  qe.enqueue("123")
  qe.enqueue("1")
  qe.enqueue("2")
  qe.enqueue("3")
  print(qe.dequeue())

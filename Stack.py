from collections import deque
from copy import deepcopy


class Stack:

  def __init__(self):
    self.stack = deque()

  def push(self, value):
    self.stack.append(value)

  def pop(self):
    return self.stack.pop()

  def peek(self):
    return self.stack[-1]

  def length(self):
    return len(self.stack)


# reverse string

string = "deepcopy"
s = Stack()
for iter in string:
  s.push(iter)
result = ""
t = deepcopy(s)
for iter in t.stack:
  result += s.pop()

print(result)

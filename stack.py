class Stack:
  def __init__(self):
    self.items = []

  def is_empty(self):
    return not self.items

  def push(self, item):
    self.items.append(item)

  def pop(self):
    return self.items.pop()

  def peek(self):
    return self.items[-1]

  def size(self):
    return len(self.items)

  # Used to inspect stack in print statement
  def __str__(self):
    return str(self.items)

# Code used if class is the main
if __name__ == "__main__":
  stack = Stack()
  print(stack)
  print(stack.is_empty())
  stack.push(3)
  stack.push(4)
  stack.push(5)
  print(stack)
  print(stack.pop())
  print(stack.peek())
  print(stack.size())

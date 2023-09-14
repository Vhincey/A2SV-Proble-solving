class MyStack:

    def __init__(self):
      self.queue = deque()
      self.size = 0

    def push(self, x: int) -> None:
      self.queue.append(x)
      self.size += 1

    def pop(self) -> int:
      if self.queue:
        self.size -= 1
        return self.queue.pop()
          

    def top(self) -> int:
      return self.queue[-1]
        
    def empty(self) -> bool:
        if self.size == 0:
          return True
        return False
# Method 2

class Node():
  def __init__(self, val):
    self.val = val
    self.next = None

class MyStack(object):

    def __init__(self):
        self.size = 0
        self.head = None

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        node = Node(x)

        node.next = self.head
        self.head = node
        self.size += 1

    def pop(self):
        """
        :rtype: int
        """
        if self.size == 0:
          return
        else:
          save = self.head.val
          self.head = self.head.next
          self.size -= 1
          return save

    def top(self):
        """
        :rtype: int
        """
        if self.size:
          return self.head.val

    def empty(self):
        """
        :rtype: bool
        """
        return self.size == 0
          
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

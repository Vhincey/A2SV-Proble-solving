class MyQueue:

    def __init__(self):
        self.stack = []
        self.size = 0        

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.size += 1

    def pop(self) -> int:
        self.size -= 1
        return self.stack.pop(0)
        
    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return self.size == 0

    # Method 2

      class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyQueue(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        node = Node(x)
        if self.size == 0:
            self.head = node
        else:
            cur = self.head
            while cur and cur.next:
                cur = cur.next
            cur.next = node
        self.size += 1        

    def pop(self):
        """
        :rtype: int
        """
        # if self.size == 0:
        #     return False
        # out = self.head.val
        # if self.size == 1:
        #     self.head = None
        # else:
        #     cur = self.head
        #     self.head = cur.next
        # self.size -= 1
        # return out
        if self.size:
            out = self.head.val
            cur = self.head
            self.head = cur.next
        self.size -= 1
        return out

    def peek(self):
        """
        :rtype: int
        """
        return self.head.val

    def empty(self):
        """
        :rtype: bool
        """
        return self.size == 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.maxsize = k
        self.size = 0
        self.head = None
        self.tail = None
        

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.size < self.maxsize:
            node = Node(value)

            if self.head:
                self.tail.next = node
                self.tail = node
            else:
                self.head = self.tail = node
            
            self.tail.next = self.head
            self.size += 1
            return True
        return False

    def deQueue(self):
        """
        :rtype: bool
        """
        
        if self.size == 0:
            return False
        
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head

        self.size -= 1
        return True  

         
    def Front(self):
        """
        :rtype: int
        """
        return self.head.value if self.head else -1
        

    def Rear(self):
        """
        :rtype: int
        """
        return self.tail.value if self.head else -1

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.size == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return self.size == self.maxsize
            


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

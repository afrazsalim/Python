class Stack:

    def __init__(self):
        self.list = None
        self.counter = 0


    def isEmpty(self):
        return self.counter == 0

    def size(self):
        return self.counter


    def push(self,item):
        if self.list is None:
           self.list = Node(item)
           self.counter = 1
        else:
           newNode = Node(item)
           newNode.next = self.list
           self.list = newNode
           self.counter = self.counter + 1


    def pop(self):
        if self.list is None:
            print("Empty stack,underflow")
        else:
            tempNode = self.list
            self.list = tempNode.next
            self.counter =self.counter - 1
            return tempNode.item






class Node:

   def __init__(self,item):
       self.item = item
       self.next = None


   def getItem(self):
       return self.item


   def hasNext(self,Node):
       return Node.next is not None



stack = Stack()
stack.push(20)
stack.push(30)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

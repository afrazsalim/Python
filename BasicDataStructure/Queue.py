class Queue:

    def __init__(self):
        self.list = None
        self.counter = 0


    def isEmpty(self):
        return self.counter == 0

    def size(self):
        return self.counter


    def enqueue(self,item):
        if self.list is None:
           self.list = Node(item)
           self.counter = 1
        else:
           newNode = self.list
           while(not(newNode.next is None)):
               newNode = newNode.next
           newNode.next = Node(item)
           self.counter = self.counter + 1


    def dequeu(self):
        if self.list is None:
            print("Empty queue,underflow")
        else:
            tempNode = self.list
            self.list = tempNode.next
            self.counter =self.counter - 1
            self.counter = self.counter - 1
            return tempNode.item






class Node:

   def __init__(self,item):
       self.item = item
       self.next = None


   def getItem(self):
       return self.item


   def hasNext(self,Node):
       return Node.next is not None

queue = Queue()
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(50)
print(queue.dequeu())
print(queue.dequeu())


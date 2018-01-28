
class Bag:
    def __init__(self,element):
        self.list = []
        self.counter = 0;
        self.list.insert(self.counter,element)
        self.counter = self.counter + 1



    def getValues(self):
        return self.list

    def add(self,newElement):
        self.list.insert(self.counter,newElement)
        self.counter = self.counter + 1

    def isEmpty(self):
        return self.counter == 0



print("Executing")
bag = Bag(1)
bag.add(20)
newList = bag.getValues()
for i in range(len(newList)):
    print(newList[i])

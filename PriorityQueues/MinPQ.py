class MinPQ:

    def __init__(self,size):
        self._counter = 1
        self._list = [None]*size



    def size(self):
        return self._counter

    def isEmpty(self):
        return self._counter <= 1


    def insert(self,item):
        self._list[self._counter] =item
        self._counter = self._counter + 1
        self._swim(self._counter-1,self._list)



    def delMin(self):
        if (self._counter <= 1) :
            print("Queue underflow")
            return -1
        returnItem = self._list[1]
        tempCounter = self._counter-1
        if (tempCounter > 1) :
            self._list[1] = self._list[tempCounter]
            self._counter = tempCounter
        else:
            self._counter = self._counter-1
        self._sink(1,self._list)
        return returnItem



    def _swim(self,counter,list):
         k = counter//2
         while(k >= 1):
             if (self.less(list[counter],list[k])):
                 self.swap(list,counter,k)
                 counter = k
                 k = k//2
             else:
                 break


    def _sink(self,item,newList):
        index = item
        j = 2*index
        while(2*index <= (len(newList))):
            if (j < len(newList) and self.less(newList[j+1],newList[j])):
                  j = j+1
            if (self.less(newList[j],newList[index])):
                self.swap(newList,index,j)
                index = index*2
            else:
                break

    def swap(self,list,first,second):
        temp = list[first]
        list[first] = list[second]
        list[second] = temp


    def less(self,first,second):
        return first < second



pq = MinPQ(100)
pq.insert(20)
pq.insert(10)
pq.insert(1)
pq.insert(-2)
pq.insert(100)
print(pq.delMin())
print(pq.delMin())
print(pq.delMin())

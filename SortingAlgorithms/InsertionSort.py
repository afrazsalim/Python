class InsertionSort:

    def sort(self,list):
       for i in range(len(list)):
           for j in range(i,0,-1):
               if list[j] < list[j-1]:
                   self.exchange(list,j-1,j)
               else:
                   break
       return list


    def exchange(self,list,i,j):
        temp = list[i]
        list[i] = list[j]
        list[j] = temp



sort = InsertionSort()
list = [9,8,7,4,5,6,1,2,3]
newList = sort.sort(list)
print(newList)

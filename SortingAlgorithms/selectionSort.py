class SelectionSort:


    def sort(self,list):
        for i in range (len(list)-1):
            tempValue = i
            for j in range (i+1,(len(list))):
                if list[j] < list[tempValue]:
                    tempValue = j
            self.swap(list,i,tempValue)
        return list


    def swap(self,list,i,j):
        temp = list[i]
        list[i] = list[j]
        list[j] = temp


sort = SelectionSort()
list = [4,5,6,8,7,4,6]
newList = sort.sort(list)
print(newList)

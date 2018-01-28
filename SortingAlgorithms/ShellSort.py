class ShellSort:


    def sort(self,list):
        h = 1
        while(h <= (len(list))//3):
            h = 3*h + 1
        while(h >= 1):
         for i in range(h,len(list)):
            j = i
            while(j >= h):
                if list[j] < list[j-h]:
                   self.exchange(list,j,j-h)
                   j = j - h
                else:
                    break
         h = h //3
        return list


    def exchange(self,list,i,j):
        temp = list[i]
        list[i] = list[j]
        list[j] = temp

sort = ShellSort()
list = [9,8,7,4,5,6,20]
newList =sort.sort(list)
print(newList)

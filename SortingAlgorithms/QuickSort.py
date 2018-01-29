
class Quicksort:

    def __init__(self,list):
        self.sort(list,0,(len(list))-1)
        self.list = list


    def sort(self,list,lo,high):
        if high <= lo:
            return
        pElem = self.partition(list,lo,high)
        self.sort(list,lo,pElem-1)
        self.sort(list,pElem+1,high)


    def partition(self,list,lo,hi):
        pivot = list[lo]
        i = lo+1
        j = hi
        while(True):
            while(self.less(list[i],pivot)):
                if (i == hi):
                    break
                i = i+1

            while(self.less(pivot,list[j])):
               if(j == lo):
                 break
               j = j-1

            if(i >= j):
                break
            self.exchange(list,i,j)
        self.exchange(list,lo,j)
        return j


    def exchange(self,list,p,q):
        temp = list[p]
        list[p] = list[q]
        list[q] = temp

    def less(self,first,second):
        if first == second:
            return False
        else:
            return first < second




list = [8,7,4,5,6,1,2,3]
print("sorting values")
sort = Quicksort(list)
print(sort.list)

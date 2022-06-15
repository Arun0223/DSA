class Sort:
    def __init__(self,my_list):
        self.my_list=my_list
    def bubble_sort(self):
        for i in range(len(self.my_list)-1,0,-1):
            for j in range(i):
                if self.my_list[j] > self.my_list[j+1]:
                    temp = self.my_list[j]
                    self.my_list[j] = self.my_list[j+1]
                    self.my_list[j+1] = temp
        return self.my_list
    def selection_sort(self):
        for i in range(len(self.my_list)-1):
            min_index=i
            for j in range(i+1,len(self.my_list)):
                if self.my_list[j] < self.my_list[min_index]:
                    min_index=j
            temp=self.my_list[min_index]
            self.my_list[min_index]=self.my_list[i]
            self.my_list[i]=temp
        return self.my_list
    def insertion_sort(self):
        for i in range(1,len(self.my_list)):
            temp=self.my_list[i]
            j=i-1
            while temp < self.my_list[j] and j>=0:
                self.my_list[j+1]= self.my_list[j]
                self.my_list[j]=temp
                j-=1
        return self.my_list

s=Sort([4,5,2,1,7])
s.bubble_sort()
s.selection_sort()
s.insertion_sort()

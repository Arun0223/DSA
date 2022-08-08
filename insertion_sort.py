my_list=list(map(int,input().split(' ')))
def insertion_sort(my_list):
	for i in range(1,len(my_list)):
		temp=my_list[i]
		j=i-1
		while my_list[j+1] < my_list[j]:
			my_list[i]=my_list[j]
			my_list[j]=temp
			j-=1
	print(my_list)
insertion_sort(my_list)

my_list=list(map(int,input().split(' ')))
def selection_sort(my_list):
	for i in range(len(my_list)-1):
		min_index=i
		for j in range(i+1,len(my_list)):
			if my_list[j] < my_list[min_index]:
				min_index=j
		temp=my_list[min_index]
		my_list[min_index]=my_list[i]
		my_list[i]=temp
	print(my_list)


selection_sort(my_list)


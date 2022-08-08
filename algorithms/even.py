def print_even(n):
	for i in range(1,n+1):
		if i%2==0:
			print(i)


def check_even(n):
	if n%2==0:
		return 'Even'
	else:
		return 'Odd'

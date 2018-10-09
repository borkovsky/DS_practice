def sortArrayByParity(A):
	A_even  = []
	A_odd = []
	for elem in A:
		if elem % 2 == 0:
			A_even.append(elem)
		else:
			A_odd.append(elem)
	return (A_even+A_odd)
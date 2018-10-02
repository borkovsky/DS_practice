def case_swap(s):
	swapped = []
	for elem in list(s):
		if elem.istitle():
			swapped.append(elem.lower())
		else:
			wapped.append(elem.upper())
	return ''.join(swapped)
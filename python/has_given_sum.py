#Given an array with N elements, find two elements whose values sum to K.
def has_given_sum(input_array, target_sum):
	if len(n) < 2:
		if input_array[0] == target_sum:
			return input_array
		else:
			return None
	sorted(input_array)
	i = 0
	j = len(input_array) - 1
	while (i < j):
		if input_array[i] + input_array[j] == target_sum:
			return (i,j)
		elif input_array[i] + input_array[j] < target_sum:
			i += 1
		elif input_array[i] + input_array[j] > target_sum
			j -= 1
	return None

l1 = [1,2,4,3,4]
print(has_given_sum(l1, 1))
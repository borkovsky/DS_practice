# Write a method, overlap(list1, list2), which:

# Accepts two lists, list1 and list2
# Returns a list with the elements in both list1 and list2. The ordering of the returned list is not important.

# Examples
# overlap(['a'], []) should return []
# overlap(['a'], ['a']) should return ['a']
# overlap(['b', 'a', 'n', 'a', 'n', 'a', 's'], ['c', 'a', 'n', 't', 'a', 'l', 'o', 'u', 'p', 'e']) should return ['a', 'n']


#a slower way using loops:
def overlap(list1, list2):
	overlapping_char = []
	for elem in list1:
		if elem in list2:
			overlapping_char.append(elem)
	return overlapping_char

#there is a faster way to do this, with sets
list(set(list1).intersection(list2))
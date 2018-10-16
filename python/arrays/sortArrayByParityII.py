# Leetcode problem: https://leetcode.com/problems/sort-array-by-parity-ii/description/

# Given an array A of non-negative integers, half of the integers in A are odd, 
# and half of the integers are even.
# Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
# You may return any answer array that satisfies this condition.

def sortByParity(a):
	even_a = []
	odd_a = []
	for elem in a:
		if elem % 2 == 0:
			even_a.append(elem)
		else:
			odd_a.append(elem)
	sorted_a = []
	for i in range(int(len(a)/2)):
		sorted_a.append(even_a.pop())
		sorted_a.append(odd_a.pop())
	return sorted_a
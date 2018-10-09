#find fibonacci recursively
def find_fibonacci(n):
	if n == 0 or n == 1:
		return n
	return find_fibonacci(n-1)+find_fibonacci(n-2)
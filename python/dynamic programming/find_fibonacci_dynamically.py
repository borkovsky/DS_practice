#dynamically
fibonacci_results = {}

def cached_find_fibonnaci(n):
	if n in fibonacci_results:
		return fibonacci_results[n]
	result = cached_find_fibonnaci(n-1)
	fibonacci_results[n] = result

	return result 
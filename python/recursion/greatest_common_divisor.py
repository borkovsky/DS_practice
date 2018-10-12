# Greatest Common Divisor
# 98   56
# Euclidian algorithm

# 98 - 56
# 56 42

# 42 14
# 28 14
# 14 0

def greatest_common_divisor(num1, num2):
	if num2 == 0:
		return num1
	else:
		gcd = greatest_common_divisor(num2, num1 % num2)
		return gcd
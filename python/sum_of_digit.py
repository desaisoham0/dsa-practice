def sum_of_digit(n):
	if not isinstance(n, int):
		raise TypeError("Please enter positive integers")
	if n < 0:
		raise ValueError("Please enter positive integers")
	if n == 0:
		return 0

	last = n % 10
	rest = n // 10
	return last + sum_of_digit(rest)

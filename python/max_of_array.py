def max_of_array(arr):
	if len(arr) == 1:
		return arr[0]
	first = arr[0]
	rest_max = max_of_array(arr[1:])
	return first if first > rest_max else rest_max

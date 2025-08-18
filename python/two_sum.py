def two_sum(nums, target):
	idx = {}
	for i, n in enumerate(nums):
		if target - n in idx:
			return [idx[target - n], i]
		idx[n] = i

	return None

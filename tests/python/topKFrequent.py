def topKFrequent(nums, k):
	freq = {}
	
	for num in nums:
		if num not in freq:
			freq[num] = 0
		freq[num] += 1

	sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
	res = []
	
	for i in range(k):
		res.append(sorted_items[i][0])
	return res

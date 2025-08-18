def valid_anagram(s, t):
	if len(s) != len(t):
		return False
	s_map = {}
	t_map = {}

	for char in s:
		if char not in s_map:
			s_map[char] = 1
		s_map[char] += 1

	for char in t:
		if char not in t_map:
			t_map[char] = 1
		t_map[char] += 1
	
	return s_map == t_map

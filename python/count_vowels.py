def count_vowels(s):
	if not s:
		return 0
	vowel = {"a", "e", "i", "o", "u"}
	first = s[0]
	rest = s[1:]
	if first in vowel:
		return 1 + count_vowels(rest)
	return 0 + count_vowels(rest)

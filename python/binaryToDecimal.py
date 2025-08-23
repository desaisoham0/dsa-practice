def binaryToDecimal(s):
	if s == "":
		raise ValueError("empty binary string")
	if len(s) == 1:
		return int(s)

	first = s[0]
	rest = s[1:]
	value = int(first) + 2 * binaryToDecimal(rest)
	return value

print(binaryToDecimal("101"))  

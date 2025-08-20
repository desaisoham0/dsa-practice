def reverse_word(word):
	reversed = ""
	for letter in word:
		reversed = letter + reversed
	return reversed

def is_palindrome(word):
	return word == reverse_word(word)

def check_all_palindrome(arr):
	for word in arr:
		if not is_palindrome(word):
			return False

	return True

print(check_all_palindrome(["racecar", "shoe", "civic"]))

from python.check_all_palindrome import check_all_palindrome

def test_check_all_palindrome_true():
	assert check_all_palindrome(["racecar", "noon", "civic"]) is True

def test_check_all_palindrome_false():
	assert check_all_palindrome(["racecar", "shoe", "moon"]) is False

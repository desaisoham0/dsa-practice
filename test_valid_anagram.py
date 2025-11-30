from python.valid_anagram import valid_anagram

def test_valid_anagram_basic():
	assert valid_anagram("racecar", "carrace") == True

def test_valid_anagram_false():
	assert valid_anagram("jar", "jam") == False

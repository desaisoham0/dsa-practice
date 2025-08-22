from python.count_vowels import count_vowels

def test_count_vowels_basic():
	assert count_vowels("abcdefg") == 2

def test_count_vowels_empty():
    assert count_vowels("") == 0

def test_count_vowels_all_vowels():
    assert count_vowels("aeiou") == 5 

def test_count_vowels_no_vowels():
    assert count_vowels("rhythm") == 0



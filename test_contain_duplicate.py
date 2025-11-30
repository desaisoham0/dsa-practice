from python.contain_duplicate import contain_duplicate

def test_contain_duplicate_true():
	assert contain_duplicate([1,2,3,3]) is True

def test_contain_duplicate_false():
	assert contain_duplicate([1,2,3,4]) is False

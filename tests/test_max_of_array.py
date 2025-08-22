from python.max_of_array import max_of_array

def test_max_of_array_basic():
	assert max_of_array([1,2,3,4,9,7,6,5]) == 9


def test_max_of_array_single():
    assert max_of_array([42]) == 42

def test_max_of_array_increasing():
    assert max_of_array([1, 2, 3, 4, 5]) == 5 

def test_max_of_array_decreasing():
    assert max_of_array([5, 4, 3, 2, 1]) == 5 

def test_max_of_array_all_same():
    assert max_of_array([7, 7, 7, 7]) == 7 

def test_max_of_array_with_negatives():
    assert max_of_array([-10, -20, -3, -50]) == -3

def test_max_of_array_mixed():
    assert max_of_array([-5, 0, 15, -2, 7]) == 15 

def test_max_of_array_large_numbers():
    assert max_of_array([1000, 9999, 500, 123456]) == 123456

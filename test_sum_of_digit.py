import pytest
from python.sum_of_digit import sum_of_digit

def test_sum_of_digit_basic():
	assert sum_of_digit(123) == 6
	
def test_sum_of_digit_single():
	assert sum_of_digit(5) == 5

def test_sum_of_digit_large():
	assert sum_of_digit(999999999) == 81

def test_sum_of_digit_ValueError():
	with pytest.raises(ValueError):
		sum_of_digit(-123)

def test_sum_of_digit_TypeError():
	with pytest.raises(TypeError):
		sum_of_digit("123")

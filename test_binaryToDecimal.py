import pytest
from python.binaryToDecimal import binaryToDecimal

def test_basic():
	assert binaryToDecimal("101") == 5

def test_zero():
	assert binaryToDecimal("0") == 0

def test_long_input():
	assert binaryToDecimal("1111") == 15

def test_empty_string():
    with pytest.raises(ValueError):
        binaryToDecimal("")



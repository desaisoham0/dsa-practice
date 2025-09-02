import pytest
from python.topKFrequent import topKFrequent

def test_case():
    assert topKFrequent([1,2,1,2,1,2,3,1,3,2], 2) == [1,2]

def test_case1():
    assert topKFrequent([1], 1) == [1]

def test_case2():
    assert topKFrequent([1,1,1,2,2,3], 2) == [1,2]

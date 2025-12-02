import pytest
from python.isIsomorphic import Solution

@pytest.fixture
def solution():
    """Fixture to instntiate the solution class for each test."""
    return Solution()


# Logic test
def test_example_case_egg_old(solution):
    """Verify standard positive case from problem description."""
    assert solution.isIsomorphic("egg", "add") is True

def test_example_case(solution):
    """Verify negative case."""
    assert solution.isIsomorphic("foo", "bar") is False

def test_example_case_paper_title(solution):
    """Verify complex positive case."""
    assert solution.isIsomorphic("paper", "title") is True

# Edge Cases
def test_length_mismatch(solution):
    """Guard Clause: String of different lengths cannot be isomorphic."""
    assert solution.isIsomorphic("abc", "abcd") is False

def test_empty_strings(solution):
    """Edge Case: Two empty strings are isomorphic."""
    assert solution.isIsomorphic("", "") is True

# Parmeterized Testing 

@pytest.mark.parametrize("s, t, expected", [
    ("13", "42", True),
    ("A", "a", True),
    ("a", "a", True),
    ("aba", "baa", False),
    ("mno", "xxy", False),
    ("a" * 1000, "b" * 1000, True),
])
def test_various_scenarios(solution, s, t, expected):
    """Bulk testing for various edge cases and data types."""
    assert solution.isIsomorphic(s, t) == expected
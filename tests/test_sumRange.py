import pytest
from python.sumRange import NumArray

@pytest.fixture
def standard_num_array():
    nums = [-2, 0, 3, -5, 2, -1]
    return NumArray(nums)

@pytest.fixture
def large_num_array():
    """Returns a larger NumArray for stress testing."""
    return NumArray(list(range(1000)))  # [0, 1, 2, ... 999]

# ==========================================
# Test Cases
# ==========================================

def test_initialization_creates_prefix_sums():
    """Verify that internal structure is built correctly on init."""
    nums = [1, 2, 3]
    obj = NumArray(nums)
    # The prefix sum list should be same length as input
    assert len(obj.prefix_sum) == 3
    # Check manual calculation: [1, 3, 6]
    assert obj.prefix_sum == [1, 3, 6]

def test_example_case_one(standard_num_array):
    """Verifies the specific examples provided in the problem description."""
    # sumRange(0, 2) -> (-2) + 0 + 3 = 1
    assert standard_num_array.sumRange(0, 2) == 1

def test_example_case_two(standard_num_array):
    """Verifies the specific examples provided in the problem description."""
    # sumRange(2, 5) -> 3 + (-5) + 2 + (-1) = -1
    assert standard_num_array.sumRange(2, 5) == -1

def test_example_case_three(standard_num_array):
    """Verifies the specific examples provided in the problem description."""
    # sumRange(0, 5) -> All elements = -3
    assert standard_num_array.sumRange(0, 5) == -3

def test_single_element_query(standard_num_array):
    """Edge Case: left and right are the same index."""
    # Index 2 is value 3. Sum should be 3.
    assert standard_num_array.sumRange(2, 2) == 3

def test_full_range_query(standard_num_array):
    """Edge Case: Querying the entire array."""
    # Sum of [-2, 0, 3, -5, 2, -1] is -3
    assert standard_num_array.sumRange(0, 5) == -3

def test_first_element_only(standard_num_array):
    """Edge Case: Querying index 0 to 0 (Boundary condition)."""
    assert standard_num_array.sumRange(0, 0) == -2

def test_large_input_logic(large_num_array):
    """Sanity check on a larger dataset."""
    # Sum of 0 to 4 is 0+1+2+3+4 = 10
    assert large_num_array.sumRange(0, 4) == 10
    
    # Sum of 10 to 12 is 10+11+12 = 33
    assert large_num_array.sumRange(10, 12) == 33

# ==========================================
# Parameterized Testing (Advanced)
# ==========================================

@pytest.mark.parametrize("nums, left, right, expected", [
    ([10], 0, 0, 10),                 # Single element array
    ([-5, -5], 0, 1, -10),            # Negative numbers
    ([0, 0, 0], 0, 2, 0),             # Zeros
    ([1, 2, 3, 4, 5], 1, 3, 9),       # Middle slice (2+3+4)
])
def test_various_scenarios(nums, left, right, expected):
    obj = NumArray(nums)
    assert obj.sumRange(left, right) == expected

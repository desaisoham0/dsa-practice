class NumArray:
    def __init__(self, nums: list[int]):
        # Create the new list to hold the running totals
        self.prefix_sum = []
        current_total = 0

        for num in nums:
            current_total += num
            self.prefix_sum.append(current_total)

    def sumRange(self, left: int, right: int) -> int:
        # Edge case: when left is at zero return only right
        if left == 0:
            return self.prefix_sum[right]
        
        return self.prefix_sum[right] - self.prefix_sum[left - 1]
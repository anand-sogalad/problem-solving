class Solution:
    def max_consecutive_one(self, nums: list[int]) -> int:
        max_ones, current_max = 0, 0
        for num in nums:
            if num == 1:
                current_max += 1
            else:
                max_ones = max(max_ones, current_max)
                current_max = 0
        return max(max_ones, current_max)

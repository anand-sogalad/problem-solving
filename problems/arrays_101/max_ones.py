"""
Max Consecutive Ones
"""


class Solution:
    def max_ones(self, arr: list[int]):
        max_ones, current_max = 0, 0
        for num in arr:
            if num == 1:
                current_max += 1
            else:
                max_ones = max(max_ones, current_max)
                current_max = 0
        return max(current_max, max_ones)

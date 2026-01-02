from typing import Literal

from problem_solving.decorators.preformance import timer


class Solution:
    @timer
    @staticmethod
    def max_consecutive_ones(nums: list[Literal[0] | Literal[1]]) -> int:
        largest = 0
        current = 0
        for num in nums:
            if num == 1:
                current += 1
            else:
                largest = max(current, largest)
                current = 0
        return max(largest, current)

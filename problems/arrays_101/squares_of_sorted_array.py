"""
Squares of a Sorted Array
"""


class Solution:
    def sortedSquares(self, nums: list[int]):
        return sorted([num**2 for num in nums])

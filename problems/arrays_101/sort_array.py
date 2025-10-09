"""
Sort Array By Parity

Solution
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.
"""


class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        write_idx = 0
        for read_idx in range(len(nums)):
            if nums[read_idx] % 2 == 0:
                nums[write_idx], nums[read_idx] = nums[read_idx], nums[write_idx]
                write_idx += 1
        return nums

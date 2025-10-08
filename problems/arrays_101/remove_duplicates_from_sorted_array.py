"""
Remove Duplicates from Sorted Array
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] == nums[i]:
                del nums[i]
        return len(nums)

"""
Remove Element
"""

from operator import le


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                del nums[i]
        return len(nums)


if __name__ == "__main__":
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = Solution().removeElement(nums, 2)
    print(nums)

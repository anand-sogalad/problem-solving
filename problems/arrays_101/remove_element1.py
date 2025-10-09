"""
Remove Element

Solution
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:
"""


# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        write_idx = 0
        for read_idx in range(len(nums)):
            if nums[read_idx] != val:
                nums[write_idx] = nums[read_idx]
                write_idx += 1
        return write_idx

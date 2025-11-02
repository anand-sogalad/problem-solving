# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.


class Solution:
    def deplicate_zeros(self, nums: list[int]):
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.insert(i, 0)
                del nums[-1]
                i += 2
            else:
                i += 1

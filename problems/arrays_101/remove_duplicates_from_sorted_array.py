"""
Remove Duplicates from Sorted Array
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] == nums[i]:
                del nums[i]
        return len(nums)


# with 0(1) and 0(n) time
class Solution1:
    def removeDuplicates(self, arr: list[int]) -> list[int]:
        write_pointer = 1
        for read_pointer in range(1, len(arr)):
            if arr[read_pointer] != arr[write_pointer - 1]:
                arr[write_pointer] = arr[read_pointer]
                write_pointer += 1
        del arr[write_pointer:]
        return arr

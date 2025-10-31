"""
Remove Element
"""


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                del nums[i]
        return len(nums)


class Solution:
    def removeElement(self, nums: list[int], val: int):
        write_index = 0
        for read_index in range(len(nums)):
            if nums[read_index] != val:
                nums[write_index] = nums[read_index]
                write_index += 1
        return write_index


if __name__ == "__main__":
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = Solution().removeElement(nums, 2)
    print(nums)

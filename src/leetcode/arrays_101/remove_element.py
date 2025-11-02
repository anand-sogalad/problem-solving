class Solution:
    def remove_element(self, nums: list[int], el: int):
        write = 0
        for read in range(len(nums)):
            if nums[read] != el:
                nums[write] = nums[read]
                write += 1
        del nums[write:]
        return nums

class Solution:
    def remove_duplicates_from_sorted_array(self, nums: list[int]):
        write = 1
        for read in range(1, len(nums)):
            if nums[read] != nums[read - 1]:
                nums[write] = nums[read]
                write += 1
        del nums[write:]
        return nums

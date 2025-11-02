from array import ArrayType


class Solution:
    def valid_mountain(self, nums: list[int]):
        middle = nums.index(max(nums))
        arr_len = len(nums)

        if arr_len < 2 or middle == 0 or middle == arr_len - 1:
            return False

        for i in range(1, middle):
            if not nums[i] < nums[i - 1]:
                return False

        for i in range(middle, arr_len - 1):
            if not nums[i] > nums[i + 1]:
                return False

        return True

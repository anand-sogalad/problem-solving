"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
"""


class Solution:
    # two pointers patterns
    def solution1(self, nums: list[int]):
        # in place replacement
        for i in range(len(nums)):
            nums[i] *= nums[i]
        return sorted(nums)  # creates new list

    def solution2(self, nums: list[int]):
        # pythonic way
        return sorted([i * i for i in nums])  # creates new list

    def solution3(self, nums: list[int]):
        left, right = 0, len(nums) - 1
        result = [0] * len(nums)
        pos = len(nums) - 1

        while left <= right:
            left_value = nums[left] ** 2
            right_value = nums[right] ** 2

            if left_value > right_value:
                result[pos] = left_value
                left += 1
            else:
                result[pos] = right_value
                right -= 1
            pos -= 1

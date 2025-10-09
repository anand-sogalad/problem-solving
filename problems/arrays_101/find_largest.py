# find largest


class Solution:
    def largest(self, nums: list[int]) -> int:
        return max(nums)


# second_largest
class solution:
    def second_largest(self, nums: list[int]):
        i = j = float("-inf")
        for k in nums:
            if k > i:
                j = i
                i = k
            elif k > j and k != i:
                j = k
        return j


# third largest
class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        first = second = third = float("-inf")

        for num in nums:
            if num > first:
                third, second, first = second, first, num
            elif num > second and num != first:
                third, second = second, num
            elif num > third and num != second and num != first:
                third = num

        return third if third != float("-inf") else first

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        final, current = 0, 0
        for num in nums:
            if num == 1:
                current += 1
            else:
                final = max(final, current)
                current = 0

        return max(final, current)

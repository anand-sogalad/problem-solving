"""
Move Zeroes

Solution
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""


class Solution:
    def moveZeroes(self, arr: list[int]):
        write_pointer = 0
        for read_pointer in range(len(arr)):
            if arr[read_pointer] != 0:
                arr[read_pointer], arr[write_pointer] = (
                    arr[write_pointer],
                    arr[read_pointer],
                )

                write_pointer += 1

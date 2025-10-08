"""
Duplicate Zeros
"""


class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        idx = 0
        while idx < len(arr) - 1:
            if arr[idx] == 0:
                arr.insert(idx, 0)
                del arr[-1]
                idx += 2
            else:
                idx += 1

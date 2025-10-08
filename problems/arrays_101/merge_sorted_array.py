"""
Merge Sorted Array
"""


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        del nums1[m:]
        del nums2[n:]
        nums1 += nums2
        nums1.sort()

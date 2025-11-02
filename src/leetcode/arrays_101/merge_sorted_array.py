class Solution:
    def merge_sorted_array(self, nums1: list[int], m: int, nums2: list[int], n: int):
        del nums1[:m]
        del nums2[:n]
        nums1 += nums2
        nums1.sort()

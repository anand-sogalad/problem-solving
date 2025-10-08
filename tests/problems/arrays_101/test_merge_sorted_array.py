import pytest
from problems.arrays_101.merge_sorted_array import Solution


class TestSolution:
    @pytest.mark.parametrize(
        "nums1, m, nums2, n, expected",
        [
            # Example 1: Basic merge
            ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
            # Example 2: nums2 is empty
            ([1], 1, [], 0, [1]),
            # Example 3: nums1 is empty
            ([0], 0, [1], 1, [1]),
            # Both arrays have one element
            ([2, 0], 1, [1], 1, [1, 2]),
            # nums1 elements are all smaller
            ([1, 2, 3, 0, 0, 0], 3, [4, 5, 6], 3, [1, 2, 3, 4, 5, 6]),
            # nums1 elements are all larger
            ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6]),
            # Interleaved elements
            ([1, 3, 5, 0, 0, 0], 3, [2, 4, 6], 3, [1, 2, 3, 4, 5, 6]),
            # Duplicate elements
            ([1, 2, 3, 0, 0, 0], 3, [2, 2, 3], 3, [1, 2, 2, 2, 3, 3]),
            # All same elements
            ([2, 2, 2, 0, 0], 3, [2, 2], 2, [2, 2, 2, 2, 2]),
            # Negative numbers
            ([-3, -1, 0, 0, 0], 2, [-2, 0, 1], 3, [-3, -2, -1, 0, 1]),
            # Large difference in sizes
            ([1, 0, 0, 0, 0, 0], 1, [2, 3, 4, 5, 6], 5, [1, 2, 3, 4, 5, 6]),
            # nums2 much smaller
            ([1, 2, 3, 4, 5, 0], 5, [6], 1, [1, 2, 3, 4, 5, 6]),
            # Single element merge
            ([0], 0, [5], 1, [5]),
            # Multiple zeros
            ([0, 0, 0, 0, 0, 0], 3, [1, 2, 3], 3, [0, 0, 0, 1, 2, 3]),
            # Mix of positive and negative
            ([-1, 0, 3, 0, 0, 0], 3, [-2, 2, 4], 3, [-2, -1, 0, 2, 3, 4]),
        ],
    )
    def test_merge(
        self, nums1: list[int], m: int, nums2: list[int], n: int, expected: list[int]
    ):
        s = Solution()
        # Note: merge modifies nums1 in-place
        s.merge(nums1, m, nums2, n)
        assert nums1 == expected

import pytest
from problems.arrays_101.duplicate_zeros import Solution


class TestDuplicateZeros:
    s = Solution()

    @pytest.mark.parametrize(
        "arr, expected",
        [
            # Basic test cases
            ([1, 0, 2, 3, 0, 4, 5, 0], [1, 0, 0, 2, 3, 0, 0, 4]),
            ([1, 2, 3], [1, 2, 3]),
            ([0, 0, 0, 0], [0, 0, 0, 0]),
            # Single zero
            ([0, 1, 2, 3], [0, 0, 1, 2]),
            ([1, 0, 2, 3], [1, 0, 0, 2]),
            ([1, 2, 0, 3], [1, 2, 0, 0]),
            # Multiple zeros
            ([0, 0, 1, 2], [0, 0, 0, 0]),
            ([1, 0, 0, 2], [1, 0, 0, 0]),
            # No zeros
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([5, 4, 3, 2, 1], [5, 4, 3, 2, 1]),
            # All zeros
            ([0, 0], [0, 0]),
            ([0, 0, 0], [0, 0, 0]),
            # Single element
            ([0], [0]),
            ([5], [5]),
            # Two elements
            ([0, 1], [0, 0]),
            ([1, 0], [1, 0]),
            ([1, 2], [1, 2]),
            # Consecutive zeros at different positions
            ([0, 0, 1, 2, 3], [0, 0, 0, 0, 1]),
            ([1, 2, 0, 0, 3], [1, 2, 0, 0, 0]),
            # Zero at end
            ([1, 2, 3, 4, 0], [1, 2, 3, 4, 0]),
            # Complex pattern
            ([8, 4, 5, 0, 0, 0, 0, 7], [8, 4, 5, 0, 0, 0, 0, 0]),
            ([0, 1, 0, 2, 0, 3], [0, 0, 1, 0, 0, 2]),
        ],
    )
    def test_duplicate_zeros(self, arr: list[int], expected: list[int]):
        TestDuplicateZeros.s.duplicateZeros(arr)
        assert arr == expected

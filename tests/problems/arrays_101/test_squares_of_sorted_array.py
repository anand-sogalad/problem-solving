import pytest
from problems.arrays_101.squares_of_sorted_array import Solution


class TestSquaresOfSortedArray:
    s = Solution()

    @pytest.mark.parametrize(
        "arr, expected",
        [
            # Basic test cases
            ([1, 2, 3, 4], [1, 4, 9, 16]),
            ([0], [0]),
            ([1], [1]),
            # Negative numbers
            ([-4, -3, -2, -1], [1, 4, 9, 16]),
            ([-5, -4, -3], [9, 16, 25]),
            # Mixed positive and negative
            ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
            ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
            ([-10, -5, 0, 5, 10], [0, 25, 25, 100, 100]),
            # All zeros
            ([0, 0, 0], [0, 0, 0]),
            # Large range
            ([-10000, -5000, 0, 1, 10000], [0, 1, 25000000, 100000000, 100000000]),
            # Two elements
            ([-1, 1], [1, 1]),
            ([2, 3], [4, 9]),
            ([-5, -2], [4, 25]),
            # Mostly negative with small positive
            ([-10, -9, -8, 1, 2], [1, 4, 64, 81, 100]),
        ],
    )
    def test_squares_of_sorted_array(self, arr: list[int], expected: list[int]):
        assert TestSquaresOfSortedArray.s.sortedSquares(arr) == expected

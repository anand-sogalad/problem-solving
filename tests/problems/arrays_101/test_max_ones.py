import pytest
from problems.arrays_101.max_ones import Solution


class TestSolution:
    @pytest.mark.parametrize(
        "arr, expected",
        [
            ([1, 0, 1, 1, 0, 1], 2),
            ([0, 0, 0], 0),
            ([1, 1, 1], 3),
            ([], 0),
            ([1, 0, 1, 1, 1, 0, 1, 1], 3),
        ],
    )
    def test_max_ones(self, arr: list[int], expected: int):
        s = Solution()
        assert s.max_ones(arr) == expected
        assert s.max_ones(arr) == expected
        assert s.max_ones(arr) == expected
        assert s.max_ones(arr) == expected
        assert s.max_ones(arr) == expected

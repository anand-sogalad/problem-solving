import pytest

from problem_solving.arrays_101.max_consecutive_ones import Solution


class TestSolution:
    @pytest.mark.parametrize("input, expected", [([1, 1, 0, 1, 1, 1], 3), ([1, 0, 1, 1, 0, 1], 2)])
    def test_max_consecutive_ones(self, input, expected):
        assert Solution().findMaxConsecutiveOnes(input) == expected

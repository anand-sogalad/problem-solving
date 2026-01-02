import pytest

from problem_solving.beginners_guide.challenge_problems.problem_1480 import Solution


class TestSolution:
    @pytest.mark.parametrize(
        "input, expected",
        [
            ([1, 2, 3, 4], [1, 3, 6, 10]),
            ([1, 1, 1, 1, 1], [1, 2, 3, 4, 5]),
            ([3, 1, 2, 10, 1], [3, 4, 6, 16, 17]),
        ],
    )
    def test_problem_1480(self, input, expected):
        assert Solution.running_sum_inplace(input) == expected

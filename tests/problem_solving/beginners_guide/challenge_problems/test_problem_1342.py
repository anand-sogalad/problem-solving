import pytest

from problem_solving.beginners_guide.challenge_problems.problem_1342 import Solution


class TestSolution:
    @pytest.mark.parametrize("input, expected", [(14, 6), (8, 4), (123, 12)])
    def test_problem_1342(self, input, expected):
        assert Solution.steps_to_zero(input) == expected

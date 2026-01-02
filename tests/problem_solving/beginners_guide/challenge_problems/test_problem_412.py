import pytest

from problem_solving.beginners_guide.challenge_problems.problem_412 import Solution


class TestSolution:
    @pytest.mark.parametrize(
        "input, expected",
        [
            (3, ["1", "2", "Fizz"]),
            (5, ["1", "2", "Fizz", "4", "Buzz"]),
            (
                15,
                [
                    "1",
                    "2",
                    "Fizz",
                    "4",
                    "Buzz",
                    "Fizz",
                    "7",
                    "8",
                    "Fizz",
                    "Buzz",
                    "11",
                    "Fizz",
                    "13",
                    "14",
                    "FizzBuzz",
                ],
            ),
        ],
    )
    def test_problem_412(self, input, expected):
        assert Solution.fizz_buzz(input) == expected

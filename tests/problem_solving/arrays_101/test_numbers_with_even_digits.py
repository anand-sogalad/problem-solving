import pytest

from problem_solving.arrays_101.find_numbers_with_even_number_of_digits import Solution


class TestSolution:
    @pytest.mark.parametrize(
        "input, expected", [([12, 345, 2, 6, 7896], 2), ([555, 901, 482, 1771], 1)]
    )
    def test_numbers_with_even_number_of_digits(self, input, expected):
        assert Solution().findNumbers(input) == expected

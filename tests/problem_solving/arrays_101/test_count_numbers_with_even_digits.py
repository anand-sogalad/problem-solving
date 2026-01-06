import pytest

from problem_solving.arrays_101.count_numbers_with_even_digits import Solution


class TestSolution:
    @pytest.mark.parametrize(
        "input, expected", [([12, 345, 2, 6, 7896], 2), ([555, 901, 482, 1771], 1)]
    )
    def test_count_numbers_with_even_digits_division(self, input, expected):
        assert expected == Solution.count_numbers_with_even_digits_division(input)

    @pytest.mark.parametrize(
        "input, expected", [([12, 345, 2, 6, 7896], 2), ([555, 901, 482, 1771], 1)]
    )
    def test_count_numbers_with_even_digits_log10(self, input, expected):
        assert expected == Solution.count_numbers_with_even_digits_log10(input)

    @pytest.mark.parametrize(
        "input, expected", [([12, 345, 2, 6, 7896], 2), ([555, 901, 482, 1771], 1)]
    )
    def test_count_numbers_with_even_digits_string(self, input, expected):
        assert expected == Solution.count_numbers_with_even_digits_string(input)

import pytest
from problems.arrays_101.even_number_digits import Solution


class TestNumberWithEvenDigits:
    s = Solution()

    @pytest.mark.parametrize(
        "arr, expected", [([123, 321, 1234, 5678], 2), ([1, 12, 32, 456, 6780], 3)]
    )
    def test_normal_method(self, arr: list[int], expected: int):
        assert TestNumberWithEvenDigits.s.numbers_with_even_digits(arr) == expected

    @pytest.mark.parametrize(
        "arr, expected", [([123, 321, 1234, 5678], 2), ([1, 12, 32, 456, 6780], 3)]
    )
    def test_simplified_method(self, arr: list[int], expected: int):
        assert (
            TestNumberWithEvenDigits.s.numbers_with_even_digits_simplified(arr)
            == expected
        )

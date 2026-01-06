from math import floor, log10


class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        return sum(1 for i in nums if self.is_even_digit(i))

    def get_digits(self, n: int) -> int:
        if not isinstance(n, int):
            raise ValueError("Provide only int value")
        elif n == 0:
            return 1
        elif n < 0:
            n = abs(n)

        return int(floor(log10(n))) + 1

    def is_even_digit(self, n: int) -> bool:
        return self.get_digits(n) % 2 == 0

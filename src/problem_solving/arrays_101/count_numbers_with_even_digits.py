from math import floor, log10

from problem_solving.decorators.preformance import timer


class Solution:
    @timer
    @staticmethod
    def count_digits_division(n: int) -> int:
        """
        Returns the number for digits in a given integer and raises value error if not integer
        """

        if not isinstance(n, int):
            raise ValueError("Provide only Integer value")

        if n == 0:
            return 1

        counter: int = 0
        while n > 0:
            n //= 10
            counter += 1

        return counter

    @timer
    @staticmethod
    def count_digits_log10(n: int) -> int:
        """
        Returns the number for digits in a given integer and raises value error if not integer
        """

        if not isinstance(n, int):
            raise ValueError("Provide only Integer value")

        if n == 0:
            return 1

        return int(floor(log10(n))) + 1

    @timer
    @staticmethod
    def count_digits_string(n: int) -> int:
        if not isinstance(n, int):
            raise ValueError("Provide only integer value")

        return len(str(n))

    @timer
    @staticmethod
    def count_numbers_with_even_digits_division(numbers: list[int]) -> int:
        counter = 0
        for number in numbers:
            number = int(number)

            if number < 0:
                number = abs(number)

            if Solution.count_digits_division(number) % 2 == 0:
                counter += 1

        return counter

    @timer
    @staticmethod
    def count_numbers_with_even_digits_log10(numbers: list[int]) -> int:
        counter = 0
        for number in numbers:
            number = int(number)

            if number < 0:
                number = abs(number)

            if Solution.count_digits_log10(number) % 2 == 0:
                counter += 1

        return counter

    @timer
    @staticmethod
    def count_numbers_with_even_digits_string(numbers: list[int]) -> int:
        counter = 0
        for number in numbers:
            number = int(number)

            if number < 0:
                number = abs(number)

            if Solution.count_digits_string(number) % 2 == 0:
                counter += 1

        return counter

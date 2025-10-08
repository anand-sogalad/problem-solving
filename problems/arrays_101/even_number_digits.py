"""
Find Numbers with Even Number of Digits
"""


class Solution:
    def numbers_with_even_digits(self, arr: list[int]):
        even_digits_number = 0
        for num in arr:
            if len(str(num)) % 2 == 0:
                even_digits_number += 1
        return even_digits_number

    def numbers_with_even_digits_simplified(self, arr: list[int]):
        return len([num for num in arr if len(str(num)) % 2 == 0])

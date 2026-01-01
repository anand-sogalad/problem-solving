from problem_solving.decorators.preformance import timer


class Solution:
    @timer
    @staticmethod
    def steps_to_zero(num: int) -> int:
        counter: int = 0
        while not num <= 0:
            num = num // 2 if num % 2 == 0 else num - 1
            counter += 1
        return counter

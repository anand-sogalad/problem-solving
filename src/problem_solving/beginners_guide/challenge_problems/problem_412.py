from problem_solving.decorators.preformance import timer


class Solution:
    @timer
    @staticmethod
    def fizz_buzz(num: int) -> list[str]:
        nums: list[str] = []
        for i in range(1, num + 1):
            if i % 3 == 0 and i % 5 == 0:
                nums.append("FizzBuzz")
            elif i % 3 == 0:
                nums.append("Fizz")
            elif i % 5 == 0:
                nums.append("Buzz")
            else:
                nums.append(str(i))
        return nums

class Solution:
    def numbers_with_even_digits(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                result += 1
        return result

    def pythonic_solution(self, nums: list[int]) -> int:
        return sum(1 for num in nums if len(str(num)) % 2 == 0)

    def numeric_solution(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            num = abs(num)
            if num == 0:
                continue
            else:
                digits = 0
                while num > 0:
                    digits += 1
                    num //= 10
            if digits % 2 == 0:
                result += 1
        return result


if __name__ == "__main__":
    solution = Solution()

    test_data = [12, 345, 2, 6, 7896]
    print(solution.numbers_with_even_digits(test_data))
    print(solution.pythonic_solution(test_data))
    print(solution.numeric_solution(test_data))

from problem_solving.beginners_guide.decorators.preformance import timer


class Solution:
    @timer
    @staticmethod
    def richest_customer_wealth(wealth: list[list[int]]) -> int:
        max_wealth: int = 0
        for individual in wealth:
            individual_health: int = 0
            for number in individual:
                individual_health += number
            max_wealth = max(max_wealth, individual_health)
        return max_wealth

    @timer
    @staticmethod
    def richest_customer_wealth_improved(wealth: list[list[int]]) -> int:
        return max((sum(i) for i in wealth), default=0)

    @timer
    @staticmethod
    def richest_customer_wealth_improved1(wealth: list[list[int]]) -> int:
        return max(map(sum, wealth))


if __name__ == "__main__":
    test_data = [[7, 1, 3], [2, 8, 7], [1, 9, 5]]
    result = Solution.richest_customer_wealth(test_data)
    print(f"result: {result}")

    result = Solution.richest_customer_wealth_improved(test_data)
    print(f"result: {result}")

    result = Solution.richest_customer_wealth_improved1(test_data)
    print(f"result: {result}")

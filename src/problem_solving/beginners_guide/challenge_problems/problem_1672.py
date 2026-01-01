from problem_solving.decorators.preformance import timer


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

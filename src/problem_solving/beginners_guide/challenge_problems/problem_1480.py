from problem_solving.beginners_guide.decorators.preformance import timer


class Solution:
    @timer
    @staticmethod
    def running_sum(nums: list[int]) -> list[int]:
        result: list[int] = []
        result.append(nums[0])

        for i in range(1, len(nums)):
            result.append(result[i - 1] + nums[i])

        return result

    @timer
    @staticmethod
    def running_sum_inplace(nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        return nums


if __name__ == "__main__":
    test_data: list[int] = [3, 1, 2, 10, 1]

    # this return the new list
    result = Solution.running_sum(test_data)
    print(f"result: {result}")

    # this returns the modified list
    result = Solution.running_sum_inplace(test_data)
    print(f"result: {result}")

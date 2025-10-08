"""
Valid mountain array
"""


class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        middle = arr.index(max(arr))
        arr_len = len(arr)

        if arr_len < 2 or middle == 0 or middle == arr_len - 1:
            return False

        # first half
        for i in range(middle):
            if not (arr[i] < arr[i + 1]):
                return False

        # second half
        for j in range(middle, arr_len - 1):
            if not (arr[j] > arr[j + 1]):
                return False

        return True


if __name__ == "__main__":
    arr = [0, 3, 2, 1]
    val = Solution().validMountainArray(arr)
    print(val)

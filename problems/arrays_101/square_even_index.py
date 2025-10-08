"""iven an Array of integers, return an Array where every element at an even-indexed position is squared."""


class Solution:
    def squareEvenIndex(self, arr: list[int]):
        for i in range(len(arr)):
            if i % 2 == 0:
                arr[i] *= arr[i]

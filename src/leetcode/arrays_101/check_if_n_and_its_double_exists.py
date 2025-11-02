class solution:
    def check_if_exists(self, nums: list[int]):
        seen = set()
        for i in nums:
            if i * 2 in seen or (i % 2 == 0 and i // 2 in seen):
                return True
            seen.add(i)
        return False

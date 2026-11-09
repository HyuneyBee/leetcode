from collections import Counter


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums_map = Counter(nums)
        th = len(nums) // 2

        for k,v in nums_map.items():
            if v >= th:
                return k
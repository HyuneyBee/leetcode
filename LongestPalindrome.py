from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_map = Counter(s)
        result = 0
        is_odd_check = True

        for v in s_map.values():
            r = v % 2
            if r == 1:
                if is_odd_check:
                    result += 1
                    is_odd_check = False
            result += v - r

        return result
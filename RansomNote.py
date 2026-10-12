from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_counter = Counter(ransomNote)
        m_counter = Counter(magazine)

        count = 0

        for k, v in m_counter.items():
            if r_counter.get(k, None):
                if r_counter[k] > m_counter[k]:
                    return False
                else:
                    count += 1

        return len(r_counter) == count


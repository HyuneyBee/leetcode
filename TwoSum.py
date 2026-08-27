from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check_map = {}
        for i,v in enumerate(nums):
            check = target - v
            if check in check_map:
                return [i, check_map.get(check)]
            check_map[v] = i
        return []


def main() -> None:
    result = Solution().twoSum([3,3], 6)
    print(result)


if __name__ == "__main__":
    main()
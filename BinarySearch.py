from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        s = 0
        e = len(nums) -1
        result = -1

        while s <= e:
            mid = (s + e) // 2

            if nums[mid] == target:
                result = mid
                break

            if nums[mid] < target:
                s = mid + 1

            if nums[mid] > target:
                e = mid - 1
        return result

def main() -> None:
    result = Solution().search([-1,0,3,5,9,12], 2)
    print(result)


if __name__ == "__main__":
    main()

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        if len(prices) == 2:
            value = prices[1] - prices[0]
            return value if value >= 1 else 0

        result = 0
        min_value = prices[0]
        for i in range(1, len(prices)):
            value = prices[i]
            if value < min_value:
                min_value = value
            else:
                price = prices[i] - min_value
                if price > result:
                    result = price

        return result

def main() -> None:
    result = Solution().maxProfit([1,2,4])
    print(result)


if __name__ == "__main__":
    main()
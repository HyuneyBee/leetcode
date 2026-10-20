class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        remember = {}

        def fibo(s):
            if s <= 1:
                return 1

            if remember.get(s):
                return remember.get(s)

            result = fibo(s - 2) + fibo(s - 1)
            remember[s] = result
            return result

        return fibo(n)

def main() -> None:
    result = Solution().climbStairs(6)
    print(result)


if __name__ == "__main__":
    main()
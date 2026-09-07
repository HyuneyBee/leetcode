class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = True
        palindrome_string = [i.lower() for i in s if i.isalpha() or i.isnumeric()]

        start = 0
        end = len(palindrome_string) - 1

        while start < end:
            if palindrome_string[start] != palindrome_string[end]:
                result = False
                break
            start += 1
            end -= 1

        return result

def main() -> None:
    result = Solution().isPalindrome("0P")
    print(result)


if __name__ == "__main__":
    main()

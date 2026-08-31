class Solution:
    def isValid(self, s: str) -> bool:
        opening_for = {')': '(', ']': '[', '}': '{'}
        stack = []

        for char in s:
            if char in opening_for:
                if not stack or stack.pop() != opening_for[char]:
                    return False
            else:
                stack.append(char)

        return not stack

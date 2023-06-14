# coding: utf-8


class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(': ')', '{': '}', '[': ']'}
        stack = [s[0]]
        for c in s[1:]:
            if stack and dic.get(stack[-1]) == c:
                stack.pop()
            else:
                stack.append(c)

        return not stack


print(Solution().isValid("()[]{}"))

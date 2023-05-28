# coding: utf-8

class Solution:
    def parseTernary(self, expression: str) -> str:
        i = len(expression) - 1
        stack = []
        while i >= 0:
            if expression[i] not in ["?", ":"]:
                stack.append(expression[i])
            elif expression[i] == "?":
                if expression[i-1] == "T":
                    t = stack.pop()
                    stack.pop()
                    stack.append(t)
                else:
                    stack.pop()

                i -= 1

            i -= 1

        return stack[-1]


print(Solution().parseTernary("F?1:T?4:5"))

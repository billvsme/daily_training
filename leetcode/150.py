# coding: utf-8
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        hash_map = {
            "+": lambda a, b: a+b,
            "-": lambda a, b: a-b,
            "*": lambda a, b: a*b,
            "/": lambda a, b: int(a/b)
        }
        stack = []
        for token in tokens:
            if token in hash_map.keys():
                num2 = stack.pop()
                num1 = stack.pop()
                num = hash_map[token](num1, num2)
            else:
                num = int(token)

            stack.append(num)

        return stack[-1]


tokens = ["2","1","+","3","*"]
print(Solution().evalRPN(tokens))

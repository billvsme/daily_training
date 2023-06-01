# coding: utf-8
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:

        a = []
        b = []

        def dfs(cur, values):
            if not cur:
                return

            dfs(cur.left, values)
            values.append(cur.val)
            dfs(cur.right, values)

        dfs(root1, a)
        dfs(root2, b)

        start_a = 0
        end_b = len(b) - 1

        while start_a < len(a) and end_b > 0:
            dec = a[start_a] + b[end_b] - target
            if dec == 0:
                return True
            if dec > 0:
                end_b -= 1
            if dec < 0:
                start_a += 1

        return False

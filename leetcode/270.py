# coding: utf-8
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.ans = root.val

        def dfs(cur):
            if not cur:
                return None

            a = abs(self.ans - target)
            b = abs(cur.val - target)
            if a > b:
                self.ans = cur.val
            elif a == b and self.ans > cur.val:
                self.ans = cur.val

            if cur.val > target:
                dfs(cur.left)
            elif cur.val < target:
                dfs(cur.right)

            return None

        dfs(root)

        return self.ans

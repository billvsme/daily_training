# coding: utf-8
from typing import Optional
from math import inf


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(root):
            if not root:
                return None
            if not root.left and not root.right:
                self.ans += 1
                return root.val

            l = dfs(root.left)
            r = dfs(root.right)

            if l == r == root.val or (l is None and r == root.val) or (r is None and l == root.val):
                self.ans += 1
                return root.val

            return inf

        dfs(root)

        return self.ans

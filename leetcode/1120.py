# coding: utf-8
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:

        self.max_avg = 0

        def dfs(root):
            if not root:
                return (0, 0)
            if not root.left and not root.right:
                self.max_avg = max(self.max_avg, root.val)
                return (root.val, 1)

            l = dfs(root.left)
            r = dfs(root.right)

            total = l[0] + r[0] + root.val
            count = l[1] + r[1] + 1
            avg = total / count

            self.max_avg = max(self.max_avg, avg)

            return (total, count)

        dfs(root)
        return self.max_avg

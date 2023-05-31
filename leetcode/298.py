# coding: utf-8
# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root):
            nonlocal res

            if not root:
                return 0

            l = dfs(root.left)
            r = dfs(root.right)

            ans = 1
            if root.left and root.val+1 == root.left.val:
                ans = max(ans, l+1)
            if root.right and root.val+1 == root.right.val:
                ans = max(ans, r+1)

            res = max(res, ans)
            return ans

        dfs(root)
        return res

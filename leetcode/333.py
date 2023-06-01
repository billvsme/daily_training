# coding: utf-8
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        self.max_ans = 1
        min_, max_ = float("-inf"), float("inf")

        def dfs(cur):
            if not cur:
                return max_, min_, 0

            lmin, lmax, lcount = dfs(cur.left)
            rmin, rmax, rcount = dfs(cur.right)
            print(cur.val, lmax, rmin, lcount, rcount)
            if lmax < cur.val < rmin:
                ans = lcount+rcount+1
                self.max_ans = max(self.max_ans, ans)
                return min(lmin, cur.val), max(rmax, cur.val), ans

            return min_, max_, 0

        dfs(root)

        return self.max_ans

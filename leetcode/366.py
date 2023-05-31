# coding: utf-8

from collections import defaultdict
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = defaultdict(list)

        def dfs(cur):
            if not cur:
                return 0

            l = dfs(cur.left)
            r = dfs(cur.right)

            depth = max(l, r) + 1

            res[depth].append(cur.val)
            return depth

        dfs(root)

        return list(res.values())

# coding: utf-8
import bisect
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        values = []

        def dfs(cur):
            if not cur:
                return None
            dfs(cur.left)
            values.append(cur.val)
            dfs(cur.right)

        dfs(root)

        right = bisect.bisect_left(values, target)
        left = right - 1
        res = []
        print(right)
        n = len(values)
        for i in range(k):
            if right >= n:
                res.append(values[left])
                left -= 1
            elif left >= 0 and abs(values[left] - target) < abs(values[right] - target):
                res.append(values[left])
                left -= 1
            else:
                res.append(values[right])
                right += 1

        return res


class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        cur = root
        stack = []
        res = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()

            if len(res) < k:
                res.append(cur.val)
            elif abs(res[0] - target) > abs(cur.val - target):
                res.pop(0)
                res.append(cur.val)

            cur = cur.right

        return res

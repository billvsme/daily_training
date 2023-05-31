# coding: utf-8
from collections import defaultdict, deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque()
        res = []
        level = 0
        queue.append((root, level))
        res = defaultdict(list)

        while queue:
            node, level = queue.popleft()
            res[level].append(node.val)

            if node.left:
                queue.append((node.left, level-1))
            if node.right:
                queue.append((node.right, level+1))

        items = list(res.items())
        items.sort()
        return [item[1] for item in items]

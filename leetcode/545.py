# coding: utf-8
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        def dfsleft(cur):
            if not cur:
                return None
            if not cur.left and not cur.right:
                return None

            res.append(cur.val)
            if cur.left:
                dfsleft(cur.left)
            elif cur.right and cur != root:
                dfsleft(cur.right)

        def dfsleaf(cur):
            if not cur:
                return None
            if not cur.left and not cur.right:
                res.append(cur.val)

            dfsleaf(cur.left)
            dfsleaf(cur.right)

        def dfsright(cur):
            if not cur:
                return None
            if not cur.left and not cur.right:
                return None

            if cur.right:
                dfsright(cur.right)
            elif cur.left and cur != root:
                dfsright(cur.left)
            if cur != root:
                res.append(cur.val)

        dfsleft(root)
        dfsleaf(root)
        dfsright(root)

        return res

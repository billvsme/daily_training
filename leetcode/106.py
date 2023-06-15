# coding: utf-8
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None

        n = len(postorder)
        node = TreeNode(postorder[n-1])
        index = inorder.index(postorder[n-1])

        node.left = self.buildTree(inorder[0:index], postorder[0:index])
        node.right = self.buildTree(inorder[index+1:], postorder[index:n-1])

        return node

# coding: utf-8


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.node = None

        def dfs(node, p, q):
            if node == p or node == q:
                return node
            elif not node:
                return None

            left = dfs(node.left, p, q)
            right = dfs(node.right, p, q)

            if not left and not right:
                return None
            elif not left:
                return right
            elif not right:
                return left
            else:
                return node

        return dfs(root, p, q)

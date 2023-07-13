# coding: utf-8
from collections import deque
from dataclasses import dataclass

@dataclass
class Node:
    value: int
    left: 'Node' = None
    right: 'Node' = None


def init_tree(values):
    tree, queue = Node(values[0]), deque()
    queue.append(tree)
    i = 1
    while queue:
        node = queue.popleft()
        try:
            node.left = Node(values[i])
            node.right = Node(values[i+1])
            i += 2
        except IndexError:
            break
        queue.extend([node.left, node.right])
    return tree


# 二叉树非递归，层序列、前序、中序、后序遍历
def level_order(tree):
    rest, queue, node = [], deque(), tree
    queue.append(node)
    while queue:
        node = queue.popleft()
        rest.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return rest


def level_order2(tree):
    rest, queue, node = [], deque(), tree
    queue.append(node)
    while queue:
        n = len(queue)
        for _ in range(n):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            rest.append(node.value)

    return rest


def pre_order(tree):
    rest, stack, node = [], [], tree
    while node or stack:
        while node:
            stack.append(node)
            rest.append(node.value)
            node = node.left

        node = stack.pop()
        node = node.right

    return rest

def in_order(tree):
    rest, stack, node = [], [], tree
    while node or stack:
        while node:
            stack.append(node)
            node = node.left

        node = stack.pop()
        rest.append(node.value)
        node = node.right

    return rest

def post_order(tree):
    rest, stack1, stack2, node = [], [], [], tree
    stack1.append(tree)
    while stack1:
        node = stack1.pop()
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
        stack2.append(node)

    while stack2:
        rest.append(stack2.pop().value)

    return rest


# 通过前序、中序遍历生成二叉树
def build_tree(pre_data, in_data):
    if not pre_data:
        return None
    node = Node(pre_data[0])
    cut = in_data.index(pre_data[0])
    node.left = build_tree(pre_data[1:cut+1], in_data[0:cut])
    node.right = build_tree(pre_data[cut+1:], in_data[cut+1:])
    return node

# 反转二叉树
def invert_tree(node):
    if node:
        node.left, node.right = node.right, node.left
        if node.left:
            node.left = invert_tree(node.left)
        if node.right:
            node.right = invert_tree(node.right)
    return node


def tree_code():
    tree = init_tree([1, 2, 3, 4, 5, 6, 7, 8])
    print(level_order(tree))
    print(level_order2(tree))
    print(pre_data := pre_order(tree))
    print(in_data := in_order(tree))
    print(post_order(tree))
    print(level_order(build_tree(pre_data, in_data)))
    print(level_order(invert_tree(tree)))


if __name__ == '__main__':
    tree_code()

# coding: utf-8

# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        node = Node(val=insertVal)
        if not head:
            node.next = node
            return node
        elif head.next == head:
            head.next = node
            node.next = head
            return head

        cur = head
        next_ = head.next

        while next_ != head:
            if cur.val <= insertVal and next_.val >= insertVal:
                break
            if cur.val > next_.val:
                if insertVal > cur.val or insertVal < next_.val:
                    break

            cur = next_
            next_ = next_.next

        cur.next = node
        node.next = next_

        return head

# coding: utf-8

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        cur = head

        not_9 = None
        while cur:
            if cur.val != 9:
                not_9 = cur

            cur = cur.next

        if not_9 is None:
            cur = ListNode(val=0)
            cur.next = head
            not_9 = cur
            head = cur

        not_9.val += 1
        cur = not_9.next
        while cur:
            cur.val = 0
            cur = cur.next

        return head

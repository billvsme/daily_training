# coding: utf-8

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        cur = head
        i = 1

        before = None
        while cur:
            if i % (m+n) == m:
                before = cur
                cur = cur.next
                before.next = None
            elif i % (m+n) == 0:
                before.next = cur.next
                cur = cur.next
            else:
                cur = cur.next

            i += 1

        return head

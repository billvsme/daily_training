# coding: utf-8
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        cur = head
        pre_start = cur

        end = head
        n = 1
        while end.next:
            end = end.next
            n += 1

        k = k % n
        if k == 0:
            return head

        while cur:
            if cur.next is None:
                end = cur
            if k < 0:
                pre_start = pre_start.next
            cur = cur.next
            k -= 1

        new_head = pre_start.next
        pre_start.next = None
        end.next = head

        return new_head

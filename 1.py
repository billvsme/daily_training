# coding: utf-8


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# 翻转链表
def rev(head):
    pre = head
    cur = head.next
    pre.next = None
    while cur:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp
    return pre

# 链表成对调换
# 1->2->3->4转换成2->1->4->3
def swap(head):
    if head is not None and head.next is not None:
        next_ = head.next
        head.next = swap(next_.next)
        next_.next = head
        return next_
    return head

def print_link(head):
    rest = []
    while head:
        rest.append(head.data)
        head = head.next

    print(rest)


def link_code():
    head = Node(1, None)
    node = head
    for i in range(2, 11):
        node.next = Node(i, None)
        node = node.next

    head = rev(head)
    print_link(head)

    head = rev(head)
    print_link(head)
    head = swap(head)
    print_link(head)


if __name__ == '__main__':
    link_code()

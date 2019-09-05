# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-09-05 11:59:18
"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        stack = []
        node = head
        while node:
            stack.append(node)
            node = node.next
        ret = stack.pop()
        node = ret
        while stack:
            node.next = stack.pop()
            node = node.next
        return ret


if __name__ == "__main__":
    t = Solution()
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    node.next.next.next.next = ListNode(5)
    x = t.reverseList(node)
    print(x.val, x.next.val, x.next.next.val, x.next.next.next.val)

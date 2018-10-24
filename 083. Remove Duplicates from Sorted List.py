# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-10-24 11:52:37
@Last Modified by:   tushushu
@Last Modified time: 2018-10-24 11:52:37
"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        vals = set()
        cur = head
        pre = ListNode(None)
        pre.next = head
        while cur:
            if cur.val in vals:
                pre.next = cur.next
                cur.next = None
                cur = pre.next
            else:
                vals.add(cur.val)
                pre = pre.next
                cur = cur.next
        return head

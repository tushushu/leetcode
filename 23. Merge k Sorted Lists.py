# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 16:13:46 2018

@author: Administrator
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        tmp = node = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        tmp.next = l1 if l1 else l2
        return node.next

    def mergeKLists(self, lists):
        n = len(lists)
        if n == 1:
            l1, l2 = lists[0], None
        elif n == 0:
            l1 = l2 = None
        else:
            mid = n//2
            l1 = self.mergeKLists(lists[mid:])
            l2 = self.mergeKLists(lists[:mid])
        return self.mergeTwoLists(l1, l2)

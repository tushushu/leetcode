# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 10:20:11 2018

@author: Administrator
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        res = tmp = ListNode(0)
        m = 0
        while l1 or l2 or m:
            if l1:
                m += l1.val
                l1 = l1.next
            if l2:
                m += l2.val
                l2 = l2.next
            tmp.next = ListNode(0)
            tmp = tmp.next
            m, tmp.val = divmod(m, 10)
        return res.next

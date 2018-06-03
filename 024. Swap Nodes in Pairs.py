<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 11:51:42 2018

@author: Administrator
"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        n = 0
        p = ListNode(0)
        p.next = q = head
        while q:
            if n % 2:
                p.val, q.val = q.val, p.val
            p = p.next
            q = q.next
            n += 1
        return head
=======
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 11:51:42 2018

@author: Administrator
"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        n = 0
        p = ListNode(0)
        p.next = q = head
        while q:
            if n % 2:
                p.val, q.val = q.val, p.val
            p = p.next
            q = q.next
            n += 1
        return head
>>>>>>> c9978dc9fcf21f5c72e7576e1b249d22946c4f1e

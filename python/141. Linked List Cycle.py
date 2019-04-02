# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-11-15 10:44:08
@Last Modified by:   tushushu
@Last Modified time: 2018-11-15 10:44:08
"""


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        p = head
        q = head
        while p and q and q.next:
            p = p.next
            q = q.next.next
            if p is q:
                return True
        return False
